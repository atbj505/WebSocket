//
//  RYWebSocketManager.h
//  Socket
//
//  Created by Robert on 2017/3/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface RYWebSocketManager : NSObject

+ (instancetype)shareInstance;

- (void)connect;
- (void)disConnect;
- (void)sendMsg:(NSData *)msg;
- (void)ping;

@end
