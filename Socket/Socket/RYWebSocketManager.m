//
//  RYWebSocketManager.m
//  Socket
//
//  Created by Robert on 2017/3/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import "RYWebSocketManager.h"
#import <SocketRocket/SocketRocket.h>

@interface RYWebSocketManager () <SRWebSocketDelegate>

@property (nonatomic, strong) SRWebSocket *webSocket;

@property (nonatomic, strong) NSTimer *heartBeat;

@property (nonatomic, assign) NSTimeInterval reConnectTime;

@end

@implementation RYWebSocketManager

+ (instancetype)shareInstance {
    static dispatch_once_t onceToken;
    static RYWebSocketManager *instance;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc] init];
        [instance initSocket];
    });
    return instance;
}

- (void)initSocket {
    self.webSocket = [[SRWebSocket alloc]initWithURL:[NSURL URLWithString:[NSString stringWithFormat:@"ws://%@:%d", @"120.0.0.1", 8000]]];
    
    self.webSocket.delegate = self;
    
    NSOperationQueue *queue = [[NSOperationQueue alloc]init];
    queue.maxConcurrentOperationCount = 1;
    
    [self.webSocket setDelegateOperationQueue:queue];
    
    [self.webSocket open];
}

- (void)initHeartBeat {
    dispatch_async(dispatch_get_main_queue(), ^{
        __weak typeof(self) weakSelf = self;
        self.heartBeat = [NSTimer scheduledTimerWithTimeInterval:3*60 repeats:YES block:^(NSTimer * _Nonnull timer) {
            NSLog(@"heart");
            [weakSelf sendMsg:@"heart"];
        }];
        [[NSRunLoop currentRunLoop]addTimer:self.heartBeat forMode:NSRunLoopCommonModes];
    });
}

- (void)destoryHeartBeat {
    dispatch_async(dispatch_get_main_queue(), ^{
        if (self.heartBeat) {
            [self.heartBeat invalidate];
            self.heartBeat = nil;
        }
    });
}

- (void)connect {
    self.reConnectTime = 0;
}

- (void)disConnect {
    [self.webSocket close];
}

- (void)sendMsg:(NSString *)msg {
    [self.webSocket send:msg];
    
}

- (void)reConnect {
    [self disConnect];
    
    //超过一分钟就不再重连 所以只会重连5次 2^5 = 64
    if (self.reConnectTime > 64) {
        return;
    }
    
    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, (int64_t)(self.reConnectTime * NSEC_PER_SEC)), dispatch_get_main_queue(), ^{
        self.webSocket = nil;
        [self initSocket];
    });
    
    //重连时间2的指数级增长
    if (self.reConnectTime == 0) {
        self.reConnectTime = 2;
    }else{
        self.reConnectTime *= 2;
    }
    
}

- (void)ping {
    [self.webSocket sendPing:nil];
}

#pragma mark - SRWebSocketDelegate

- (void)webSocket:(SRWebSocket *)webSocket didReceiveMessage:(id)message {
    NSLog(@"服务器返回收到消息:%@",message);
}

- (void)webSocketDidOpen:(SRWebSocket *)webSocket {
    NSLog(@"连接成功");
    
    [self initHeartBeat];
}

- (void)webSocket:(SRWebSocket *)webSocket didFailWithError:(NSError *)error {
    NSLog(@"连接失败.....\n%@",error);
    
    [self reConnect];
}

- (void)webSocket:(SRWebSocket *)webSocket didCloseWithCode:(NSInteger)code reason:(NSString *)reason wasClean:(BOOL)wasClean {
    
    NSLog(@"被关闭连接，code:%ld,reason:%@,wasClean:%d",code,reason,wasClean);
    
    //如果是被用户自己中断的那么直接断开连接，否则开始重连
    if (code == 0) {
        [self disConnect];
    }else{
        
        [self reConnect];
    }
    //断开连接时销毁心跳
    [self destoryHeartBeat];
    
}

- (void)webSocket:(SRWebSocket *)webSocket didReceivePong:(NSData *)pongPayload {
    NSLog(@"收到pong回调");
}

@end
