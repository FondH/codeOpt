#pragma once

#include<iostream>
#include<cstring>
#include<sstream>
#include<vector>
#include <limits>

// 逻辑门类型
#define XOR 0
#define AND 1
#define NOT 2
#define OR 3
#define NAND 4
#define NOR 5

// 定义输入来源类型
#define FROM_INPUT 0
#define FROM_DEVICE 1

// 全局标签计数器
int baselabel = 0;

// 获取新的标签
int GetLabel() {
	return baselabel++;
}


//	InputPool 中保留了两种数据：
//		1、原始输入，保留在inputs_0 数组
//		2、门产生的中间结果， 保留在inputs_1 数组
//	
//		this->get(type, idx)从pool中取数据， type表明是1、还是2、中获取数据
//		this->set(type, idx, val) 则相反
class InputPool {

public:
	InputPool(const int s0, const int s1);

	std::string to_string();

	int get(const int type, const int idx);

	void set(const int type, const int idx, const int val);

	void init();

	int* get_pool_array();

private:
	int s0, s1;        // 输入池的大小
	int* inputs_0;     // 输入类型0的数组
	int* inputs_1;     // 输入类型1的数组
};


//		Input 抽象的输入数据类型， 每一个Input实例化对象 都表明一个门结构的一个输入类型
//	它定义了这个‘输入’数据来自于[原始输入]还是[其他门结构]的值，同时每当门结构计算需要
//  得到输入数据时，根据这个抽象输入类型，从InputPool_ 中查询...
//		调用 get(InputPool& pool_) 在InputPool中查询。
//		
//		this->get_label() 返回来自原始输入的哪路 或 哪个门电路
//		this->get_type() 返回原始输入 or 其他门结构
class Input {

public:
	Input() :input_from(0), serial_number(0) {};
	Input(const int f, const int s) :input_from(f), serial_number(s - 1) {};
	std::string to_string();
	int get(InputPool& pool_);

	int get_type();

	int get_label();
private:
	int input_from;    // 输入来源
	int serial_number; // 输入序列号
};

//	  定义一个门结构类型， 包括其有多少输入、每个输入的类型，以及计算得到结果。
//		this->forward() 计算结果
//		pool_ 即InputPool 的实例化...
class Device {
public:

	Device() {}
	Device(const std::string str, InputPool* p = nullptr);

	std::string to_string();

	int forward(bool is_print = true);

	int* get_parents();

	int get_parents_num();

	bool check();

private:
	int type;              // 设备类型
	int label;             // 设备标签
	std::string type2str[6] = { "XOR", "AND", "NOT", "OR", "NAND", "NOR" };

	InputPool* pool_ = nullptr; // 输入池指针
	int num_input;        // 输入数量
	int num_parents;      // 父节点数量
	Input* inputs;        // 输入数组
};

bool is_all_device_pass(bool* status, const int s);

class circle {


public:
	InputPool* pool_; // 输入池指针

	//	n_input(int) : 原始输入信号的数量
	//	n_device(int): 所有门电路数量
	//  test (bool)  : true状态将所有计算过程打印，否则无
	circle(const int n_input, const int n_device, bool test = true);

	//  idx为保存逻辑门列表的编号
	//	describe为对该门的描述（具体含义见原题）: 
	//		TYPE num_input O1 I1 
	//		XOR 3 O1 O2
	void set_device(const int idx, const std::string describe);

	Device get_device(const int i);

	//  将所有逻辑门的状态输出
	std::string get_device_list();

	//  用于输入一个电路信号， idx指明了是第几路的信号， a是信号值（0 / 1）
	void input(const int a, const int idx);

	void calc();

	//  用于适应题目， 输入原始多路信号 类似 0 1 1， 通过调用output得到结果
	void input(const std::string str);

	//  测试电路是否有环
	//  return (bool): true(有环) false(无环)
	bool test_loop();

	//  得到电路输出
	//  describe: 决定输出哪些门的状态，具体见原题目要求
	//		比如: 3 2 3 4   表示输出三个状态，分别是第2、3、4个门的状态
	//  return (str): 1 0 2
	std::string output(const std::string describe);

private:
	const int n_input;    // 输入数量
	const int n_device;   // 设备数量
	Device* device_list;  // 设备列表
	bool* device_status;  // 设备状态
	bool test;            // 测试标志
};

