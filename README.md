# RasaChatbot
Rasa chatbot for finding corona cases 
I didint get the access to you provided api for the corona cases so i used different one

You can get the values by pin code and the state name only as that data contains the statewise values.

For user name you can type the names present in NLU intent my_name as for name entity lots of input data is requres.

example names[kiran,ravi,vandana,rahul,pravin]
example states [maharastra,goa,rajastan,gujrat etc...]


Sample Output

Your input ->  hi
Greetings!
what is your name?
Your input ->  my name is kiran
Hello kiran How can i help you?
Your input ->  show me the corona cases in **411048**
confirmedCasesForeign:3 ,confirmedCasesIndian:5053333discharged:4347592 ,totalCo
nfirmed:5053336 , deaths: 75277 ,
Your input ->  tell me thecorona cases in **goa**
confirmedCasesForeign:1 ,confirmedCasesIndian:116212discharged:82214 ,totalConfi
rmed:116213 , deaths: 1612 ,
Your input ->  how many corona cases?
what is your name?
Your input ->  kiran
Hello kiran How can i help you?
Your input ->  tell me corona cases?
**Did you mean results for  411048**
? Did you mean results for  411048 1: Yes (/pincode{"pin":411048})
confirmedCasesForeign:3 ,confirmedCasesIndian:5053333discharged:4347592 ,totalCo
nfirmed:5053336 , deaths: 75277 ,
Your input ->  hi
Hey there!
what is your name?
Your input ->  kiran
Hello kiran How can i help you?
Your input ->  tell me corona cases?
Did you mean results for  411048
 2: No (/<greet>)

Hi there, friend!
what is your name?
Your input ->  kiran
Hello kiran How can i help you?
Your input -> ** bored**

If you're bored, you could plan your dream vacation.
Your input ->  tell me corona cases today?
? Did you mean results for  411048 (Use arrow keys)
 » 1: Yes (/pincode{"pin":411048})
   2: No (/<greet>)
   Type out your own message...
