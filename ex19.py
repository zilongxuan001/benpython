#--coding: utf-8 --
#Date:20170824
#Title:ex19 �����ͱ���

#���庯��cheese_and_crackers()
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#��ӡ���ж��ٸ����ҡ�
	print('You have %d cheeses!'%cheese_count)
	#��ӡ�����ж��ٺб��ɡ�
	print('You have %d boxes of crackers!'%boxes_of_crackers)
	#�ۻ���˹��ˡ�
	print("Man that's enough for a party!")
	#��ӡ������̺�ӡ�
	print('Get a blanket.\n')

#��ӡ�������ܹ�ֱ�Ӹ������������֡�
print('We are just give the function numbers directly:')

#��20��30����cheese_and_crackers()�����
cheese_and_crackers(20, 30)

#��ӡ��Ŷ���ҿ��������ǽű���ı���
print('OR, we can use variables from our script:')
#��10��ֵ������amount_of_cheese
amount_of_cheese =10

#��50��ֵ������amount_of_crackers
amount_of_crackers = 50

#������amount_of_cheese,amount_of_crackers����cheese_and_crackers������
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#��ӡ�����������ܽ�����ѧ���㣬�ٴ���������
print('We can even do math inside too:')
#������10 + 20, 5+60����cheese_and_crackers������
cheese_and_crackers(10 + 20, 5+6 )

#��ӡ���������ܹ�����������ѧ���ϣ��ٴ��������
print('And we can combine the two, variables and math:')

#������amount_of_cheese+100, amount_of_crackers+1000����cheese_and_crackers������
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


# add score
#������ַ��http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# ���Ž��ű����꣬��ÿһ���������һ��ע�⣬˵�����е����á�
# �����һ�п�ʼ�������Ķ�ÿһ�У��������е���Ҫ�ַ�����
# �Լ�������һ������������Ȼ����10�ַ����������������

#����
#�Զ��庯�����б�ǩ����def ,˵����Ҫ����һ�������ˡ�
#�к������ƣ�˵����Ҫ����ĺ�����ʲô���֣���������á�
#�������ԭ�ϣ�������������Ҫ�ӹ���ԭ�ϡ�
#�в�������(������)����ԭ�Ͻ��мӹ���
#����������أ������Ǽӹ���ĳ�Ʒ��
#һ����������һ�ѵ�̵�����ԭ�Ͻ��мӹ�����̳ɷ��񣬻�����ż��
#һ����������һ��ģ�ߣ�ԭ�Ͻ�ȥ��ģ�ͳ�����
#��������һ�����ӣ��������浹��ȥʲô��������ʲô��
#�����Ĳ����������룬���ؾ����������return�����һ��ֵ��ûreturn�����һ��None.