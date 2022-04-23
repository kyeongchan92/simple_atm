# simple_atm
bearrobotics coding challenge

![image](https://user-images.githubusercontent.com/25517592/164886558-9c8e595e-6222-4ac3-9cdf-2bbbaff44051.png)


### Launching Bank
~~~
kbbank = KB_Bank()
~~~
### new customers
~~~
kbbank.enroll_new_customer(name='daniel_001', pin=1535, account=123456789, init_balance=31)
kbbank.enroll_new_customer(name='charles_843', pin=8432, account=419238122, init_balance=444)
kbbank.enroll_new_customer(name='jason_888', pin=3378, account=789456123, init_balance=6)
kbbank.add_new_account(name='charles_843', pin=8432, account=190228382, init_balance=11458)
~~~
### check bank's customer information
~~~
kbbank.data
~~~
### insert card
~~~
atm('kb_bank', 'charles_843')
~~~
~~~
[output]
charles_843, enter your pin : 
~~~
    1. ~~~

