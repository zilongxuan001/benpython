#--coding: utf-8 --
#Date:20170825
#Title:ex20 �������ļ�

#��ģ��sys����argv
from sys import argv

#��argv��ֵ��script��input_file����cmd����ʱҪ�����ļ���
script, input_file =argv

#���庯��print_all�������Ƕ�ȡһ���ļ�
def print_all(f):
	print(f.read(),'\n')

#���庯��rewind�������Ǵ��¿�ʼ��ȡ�ļ���
def rewind(f):
	f.seek(0)
#���庯��print_a_line�����������1��ֵ����ȡ�ļ�1�С�
def print_a_line(line_count,f):
	print(line_count,f.readline())

#���������ļ���ֵ��current_file
current_file = open(input_file)

#��ӡ�����ȣ����Ǵ�ӡ���е��ļ�
print("First let's print the whole file:\n")

#����print_all����ӡ�ļ���������
print_all(current_file)

#��ӡ�����ڣ����������¶�ȡ������¼������
print("Now let's rewind,kind of like a tape.\n")

#��ָ��ָ���ļ���һ��
rewind(current_file)

#��ӡ�������ǿ�ʼ��ӡ����
print("Let's print three lines:")

#��1��ֵ��current_line
current_line = 1
#��current_line��current_file����print_a_line����ӡ1�͵�һ��
print_a_line(current_line,current_file)

#current_line��1
current_line= current_line + 1
#��current_line��current_file����print_a_line����ӡ2�͵ڶ���
print_a_line(current_line,current_file)

#current_line��1
current_line= current_line+1
#��current_line��current_file����print_a_line����ӡ3�͵�����
print_a_line(current_line,current_file)

#��ָ�붨λ�ڵ�һ�У�ƫ��2���ַ����ӵ�һ�е������ַ���ʼ
current_file.seek(2,0)

#��ӡ���ļ���һ�У��ӵ�һ�е������ַ���ʼ��ȡ��
print('\n',current_file.readline())
#��ӡ����ӡʣ�ಿ�֡�
print('\n',current_file.read())


 

#file.seek(),seek�Ǹ�ָ�룬ָ���ļ��ĸ��У�file.seek()�������ļ���ͷ��ʼ��ȡ����file.seek ,��f.readline()�޶�ȡ�����ݡ�
#seek()Ĭ��ֵ��0����˼Ϊָ���ļ���ͷ��
#ֵΪ1����ӵ�ǰλ�ÿ�ʼ��ֵΪ2������ָ����ĩ����λ�á�

# add score
#������ַ��http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# ͨ���ű�����ÿ��֮ǰ����ע�⣬�����ű��﷢�������顣
# ÿ�� print_a_line ����ʱ���㶼������һ���� current_line �ı�������ÿ�ε��ú���ʱ����ӡ�� current_line ��ֵ������һ������ print_a_line ����������� line_count �ġ�
# �ҳ��ű���ÿһ���õ������ĵط������ def һ�У�ȷ�ϲ���û���ô�
# �����о�һ�� file �е� seek ��������ʲô�õġ��������� pydoc file �����ܲ���ѧ�����ࡣ
# �о�һ�� += �����д�����������ã�дһ���ű�����������������������һ�¡�

#�Լ�����
#������
#current_file.seek(0)
# print('\n',current_file.readline())
# print('\n',current_file.read())
#���԰�current_file.seek(0)�ĳ�
#current_file.seek(0,1) 0��ʾ���ַ�ƫ�ƣ�1��ʾ�ӵ�ǰλ�ÿ�ʼ
#current_file.seek(2,0) 2��ʾ��ƫ��2���ַ����ӵ������ַ���ʼ��ȡ��0��ʾ��ͷ��ʼ��