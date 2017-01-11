//
//  RYSocketManager.h
//  Socket
//
//  Created by Robert on 2017/1/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface RYSocketManager : NSObject

+ (instancetype)shareInstance;

- (void)connect;
- (void)disConnect;
- (void)sendMsg:(NSString *)msg;

@end
