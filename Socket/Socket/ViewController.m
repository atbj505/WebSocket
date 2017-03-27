//
//  ViewController.m
//  Socket
//
//  Created by Robert on 2017/1/11.
//  Copyright © 2017年 Robert. All rights reserved.
//

#import "ViewController.h"
#import "RYWebSocketManager.h"
#import "ChatMessage.pbobjc.h"

@interface ViewController ()

@property (weak, nonatomic) IBOutlet UITextField *textField;

@end

@implementation ViewController

- (IBAction)connet:(UIButton *)sender {
    [[RYWebSocketManager shareInstance] connect];
}

- (IBAction)disconnect:(UIButton *)sender {
    [[RYWebSocketManager shareInstance] disConnect];
}

- (IBAction)send:(UIButton *)sender {
    [[RYWebSocketManager shareInstance] sendMsg:self.textField.text];
}

- (void)touchesEnded:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event {
    [self.textField resignFirstResponder];
}

@end
