//
//  ViewController.m
//  Socket
//
//  Created by Robert on 2017/1/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import "ViewController.h"
#import "RYSocketManager.h"
#import "RYWebSocketManager.h"
#import "ChatMessage.pbobjc.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)dealloc {
//    [[RYSocketManager shareInstance] disConnect];
    [[RYWebSocketManager shareInstance] disConnect];
}

- (void)viewDidLoad {
    [super viewDidLoad];
//    [[RYSocketManager shareInstance] connect];
    [[RYWebSocketManager shareInstance] connect];
}

- (void)touchesEnded:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
//    [[RYSocketManager shareInstance] sendMsg:@"Robert"];
    // NSData *data = [chatMessage data];
//     ChatMessage *message = [ChatMessage parseFromData:data error:nil];
    
    [[RYWebSocketManager shareInstance] sendMsg:@"Hello World"];
}

@end
