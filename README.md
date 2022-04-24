# simple_atm
bearrobotics coding challenge

![image](https://user-images.githubusercontent.com/25517592/164886558-9c8e595e-6222-4ac3-9cdf-2bbbaff44051.png)




### Process

Insert Card 

=> PIN number 

=> Select Account 

=> See Balance/Deposit/Withdraw

### 0. Define Bank, Controller
~~~
# Define Bank
kbbank = KB_Bank()

# new customers
kbbank.enroll_new_customer(name='daniel_001', pin=1535, account=123456789, init_balance=31)
kbbank.enroll_new_customer(name='charles_843', pin=8432, account=419238122, init_balance=444)
kbbank.enroll_new_customer(name='jason_888', pin=3378, account=789456123, init_balance=6)
kbbank.add_new_account(name='charles_843', pin=8432, new_account=190228382, init_balance=11458)

# Enroll bank into Controller
atm = Controller(
    [
     ('kb_bank',  kbbank)
    ]
    )
    
# check bank's customer information
kbbank.data
~~~
~~~
[output]
{1535: {123456789: 31},
 8432: {419238122: 444, 190228382: 11458},
 3378: {789456123: 6}}
~~~
### 1. Insert card
~~~
atm('kb_bank', 'charles_843')
~~~
~~~
[output]
charles_843, enter your pin : 
~~~
### 2. Check pin number
~~~
charles_843, enter your pin : 8432
~~~
~~~
[output]
Welcome charles_843.

Your accounts
419238122
190228382

Select account : 
~~~
### 3. Select account
~~~
Select account : 419238122
~~~
~~~
[output]
What task do you want? see_balance/deposit/withdraw : 
~~~
### 4. Select task
#### 4-1. see_balance
~~~
What task do you want? see_balance/deposit/withdraw : see_balance
~~~
~~~
[output]
Balance : 11458
~~~

#### 4-2. deposit
~~~
What task do you want? see_balance/deposit/withdraw : deposit
~~~
~~~
[output]
Balance : 11458
~~~
~~~
how much do you want to deposit : 30
~~~
~~~
[output]
Balance : 474
~~~

#### 4-3. withdraw
~~~
What task do you want? see_balance/deposit/withdraw : withdraw
~~~
~~~
[output]
Balance : 11458
~~~
~~~
how much do you want to withdraw : 100
~~~
~~~
[output]
Balance : 374
~~~
