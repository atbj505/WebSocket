//
//  RYSocketManager.m
//  Socket
//
//  Created by Robert on 2017/1/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import "RYSocketManager.h"
#import <CocoaAsyncSocket/GCDAsyncSocket.h>

@interface RYSocketManager () <GCDAsyncSocketDelegate>

@property (nonatomic, strong) GCDAsyncSocket *socket;

@end

@implementation RYSocketManager

+ (instancetype)shareInstance {
    static dispatch_once_t onceToken;
    static RYSocketManager *instance;
    dispatch_once(&onceToken, ^{
        instance = [[self alloc] init];
        [instance initSocket];
    });
    return instance;
}

- (void)initSocket {
    self.socket = [[GCDAsyncSocket alloc] initWithDelegate:self delegateQueue:dispatch_get_main_queue()];
}

- (void)connect {
    [self.socket connectToHost:@"127.0.0.1" onPort:9000 error:nil];
}

- (void)disConnect {
    [self.socket disconnect];
}

- (void)sendMsg:(NSString *)msg {
    NSData *data  = [msg dataUsingEncoding:NSUTF8StringEncoding];
    
    [self.socket writeData:data withTimeout:-1 tag:9000];
}

- (void)receiveMsg {
    [self.socket readDataWithTimeout:-1 tag:9000];
}

- (void)checkPingPong {
    [self.socket readDataWithTimeout:3 tag:110];
    
}

#pragma mark - GCDAsyncSocketDelegate
- (void)socket:(GCDAsyncSocket *)sock didConnectToHost:(NSString *)host port:(uint16_t)port {
    NSLog(@"连接成功,host:%@,port:%d",host,port);
    
    [self checkPingPong];
}

- (void)socketDidDisconnect:(GCDAsyncSocket *)sock withError:(nullable NSError *)err {
    NSLog(@"断开连接,host:%@,port:%d",sock.localHost,sock.localPort);
}

- (void)socket:(GCDAsyncSocket*)sock didWriteDataWithTag:(long)tag {
    NSLog(@"写的回调,tag:%ld",tag);
    [self checkPingPong];
}

- (void)socket:(GCDAsyncSocket *)sock didReadData:(NSData *)data withTag:(long)tag {
    NSString *msg = [[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding];
    NSLog(@"收到消息：%@",msg);
    
    [self receiveMsg];
}

@end
