#--coding: utf-8 --
#Date:20170822
#Title:ex15 ��ȡ�ļ�

#��sysģ���е���argv
from sys import argv

#��argv�����scipt��filename
script, filename =argv

#���ļ���
txt=open(filename)

#��ӡ����������ļ����ļ�����
print("Here's your file %r:" %filename)
#��ӡ���ļ�����
print(txt.read())

#��ӡ���ڴ�ӡ�ļ���һ��
print("Type the filename again:")
#����>���ļ�������ֵ��file_again
file_again =input(">")

#���ļ�
txt_again=open(file_again)

#��ӡ�ļ����ݡ�
print(txt_again.read())


#Ҫ����ex15.py ,Ҫ��ǰ�Ӻ��ļ� ex15_sample.txt�����ݿ���Ϊ
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.

#����ex15.py����cmd������ python ex15.py  ex15_sample.txt

# add score
#������ַ��http://old.sebug.net/paper/books/LearnPythonTheHardWay/
# ��ÿһ�е�������ע��˵����һ�е���;��
# ����㲻ȷ���𰸣����ʱ��ˣ����������������󲿷�ʱ��ֻҪ���� ��python�� ������Ҫ�ѵĶ������ܵõ���Ҫ�Ĵ𰸡���������һ�¡�python open����
# ��ʹ���ˡ��������ʣ�����ʵ�������ǵ������ǡ�������function�����͡�������method������������һ�������ߵ���������𡣿�������Ҳû��ϵ����ʧ�ڱ�ĳ���Ա��֪ʶ�������Ǻ�������һ�����顣
# ɾ�� 10-15 ��ʹ�õ� raw_input �Ĳ��֣�������һ��ű���
# ֻ���� raw_input д����ű����������ֵõ��ļ����Ƶķ������ã��Լ�Ϊʲô��
# ���� pydoc file ���¹���ֱ������ read() �������/�������������ܶ��������˰ɣ�������Ҽ������Կ�������Ҫ����Щ���� __ �������»��ߣ��������Щֻ���������ѡ�
# �ٴ����� python ����������ʹ�� open ��һ���ļ������� open �� read �ķ���Ҳֵ����һѧ��
# ����Ľű���� txt and txt_again ����ִ��һ�� close() ���������ļ�������Ҫ����رգ����Ǻ���Ҫ��һ�㡣


#pydoc�÷���windows��cmd������ python -m pydoc open
