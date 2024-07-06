#pragma once

#include<iostream>
#include<cstring>
#include<sstream>
#include<vector>
#include <limits>

// �߼�������
#define XOR 0
#define AND 1
#define NOT 2
#define OR 3
#define NAND 4
#define NOR 5

// ����������Դ����
#define FROM_INPUT 0
#define FROM_DEVICE 1

// ȫ�ֱ�ǩ������
int baselabel = 0;

// ��ȡ�µı�ǩ
int GetLabel() {
	return baselabel++;
}


//	InputPool �б������������ݣ�
//		1��ԭʼ���룬������inputs_0 ����
//		2���Ų������м����� ������inputs_1 ����
//	
//		this->get(type, idx)��pool��ȡ���ݣ� type������1������2���л�ȡ����
//		this->set(type, idx, val) ���෴
class InputPool {

public:
	InputPool(const int s0, const int s1);

	std::string to_string();

	int get(const int type, const int idx);

	void set(const int type, const int idx, const int val);

	void init();

	int* get_pool_array();

private:
	int s0, s1;        // ����صĴ�С
	int* inputs_0;     // ��������0������
	int* inputs_1;     // ��������1������
};


//		Input ����������������ͣ� ÿһ��Inputʵ�������� ������һ���Žṹ��һ����������
//	����������������롯����������[ԭʼ����]����[�����Žṹ]��ֵ��ͬʱÿ���Žṹ������Ҫ
//  �õ���������ʱ��������������������ͣ���InputPool_ �в�ѯ...
//		���� get(InputPool& pool_) ��InputPool�в�ѯ��
//		
//		this->get_label() ��������ԭʼ�������· �� �ĸ��ŵ�·
//		this->get_type() ����ԭʼ���� or �����Žṹ
class Input {

public:
	Input() :input_from(0), serial_number(0) {};
	Input(const int f, const int s) :input_from(f), serial_number(s - 1) {};
	std::string to_string();
	int get(InputPool& pool_);

	int get_type();

	int get_label();
private:
	int input_from;    // ������Դ
	int serial_number; // �������к�
};

//	  ����һ���Žṹ���ͣ� �������ж������롢ÿ����������ͣ��Լ�����õ������
//		this->forward() ������
//		pool_ ��InputPool ��ʵ����...
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
	int type;              // �豸����
	int label;             // �豸��ǩ
	std::string type2str[6] = { "XOR", "AND", "NOT", "OR", "NAND", "NOR" };

	InputPool* pool_ = nullptr; // �����ָ��
	int num_input;        // ��������
	int num_parents;      // ���ڵ�����
	Input* inputs;        // ��������
};

bool is_all_device_pass(bool* status, const int s);

class circle {


public:
	InputPool* pool_; // �����ָ��

	//	n_input(int) : ԭʼ�����źŵ�����
	//	n_device(int): �����ŵ�·����
	//  test (bool)  : true״̬�����м�����̴�ӡ��������
	circle(const int n_input, const int n_device, bool test = true);

	//  idxΪ�����߼����б�ı��
	//	describeΪ�Ը��ŵ����������庬���ԭ�⣩: 
	//		TYPE num_input O1 I1 
	//		XOR 3 O1 O2
	void set_device(const int idx, const std::string describe);

	Device get_device(const int i);

	//  �������߼��ŵ�״̬���
	std::string get_device_list();

	//  ��������һ����·�źţ� idxָ�����ǵڼ�·���źţ� a���ź�ֵ��0 / 1��
	void input(const int a, const int idx);

	void calc();

	//  ������Ӧ��Ŀ�� ����ԭʼ��·�ź� ���� 0 1 1�� ͨ������output�õ����
	void input(const std::string str);

	//  ���Ե�·�Ƿ��л�
	//  return (bool): true(�л�) false(�޻�)
	bool test_loop();

	//  �õ���·���
	//  describe: ���������Щ�ŵ�״̬�������ԭ��ĿҪ��
	//		����: 3 2 3 4   ��ʾ�������״̬���ֱ��ǵ�2��3��4���ŵ�״̬
	//  return (str): 1 0 2
	std::string output(const std::string describe);

private:
	const int n_input;    // ��������
	const int n_device;   // �豸����
	Device* device_list;  // �豸�б�
	bool* device_status;  // �豸״̬
	bool test;            // ���Ա�־
};

