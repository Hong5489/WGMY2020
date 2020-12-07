# babyrev
Description
> Simple baby reverse challenge to get started!

Attachment:
- [babyrev](babyrev)

Its a ELF file (Linux executable file)
```bash
file babyrev 
babyrev: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0d3189284d68e7952dd33d55799f885e320089b9, for GNU/Linux 3.2.0, not stripped
```
Try run to it:
```
./babyrev 
Enter password: flag
The password must be in length of 32!

./babyrev 
Enter password: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Incorrect password!
```
Looks like the password is in length of 32

Lets try use `ltrace` command
```bash
ltrace ./babyrev 
printf("Enter password: ")                                                         = 16
__isoc99_scanf(0x55688cebc019, 0x7fff9b526d10, 0, 0Enter password: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
)                               = 1
strlen("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"...)                                      = 32
strncmp("7gg`h3gb0e6f3f1gggf567c4g`325n5b"..., "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"..., 32) = -42
puts("Incorrect password!"Incorrect password!
)                                                        = 20
+++ exited (status 0) +++
```
Looks like it compare our password with some weird character

If I change my input it compare with different text:
```bash
ltrace ./babyrev 
printf("Enter password: ")                                                         = 16
__isoc99_scanf(0x55d7b9586019, 0x7ffd4ddf8e70, 0, 0Enter password: bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
)                               = 1
strlen("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"...)                                      = 32
strncmp("4ddck0da3f5e0e2ddde654`7dc016m6a"..., "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"..., 32) = -46
puts("Incorrect password!"Incorrect password!
)                                                        = 20
+++ exited (status 0) +++
```

Enough for trying, lets decompile it with Ghidra!

Main function:
```c
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  byte local_68 [27];
  char acStack77 [21];
  byte local_38 [44];
  int local_c;
  
  printf("Enter password: ");
  __isoc99_scanf(&DAT_00102019,local_38);
  sVar2 = strlen((char *)local_38);
  if (sVar2 == 0x20) {
    local_c = 0;
    while (local_c < 0x20) {
      local_68[local_c] = local_38[SHUFFLE[local_c]];
      local_68[local_c] = local_68[local_c] ^ XOR[local_c];
      local_c = local_c + 1;
    }
    iVar1 = strncmp((char *)local_68,(char *)local_38,0x20);
    if ((iVar1 == 0) && (iVar1 = strncmp(acStack77,"15963",3), iVar1 == 0)) {
      printf("Correct password! The flag is wgmy{%s}",local_38);
    }
    else {
      puts("Incorrect password!");
    }
  }
  else {
    puts("The password must be in length of 32!");
  }
  return 0;
}
```
Let me explain part by part

First, it ask for your password input then put in `local_38`:
```c
printf("Enter password: ");
__isoc99_scanf(&DAT_00102019,local_38);
```
Then it check if the input length is equal 32, if not it put the message:
```c
sVar2 = strlen((char *)local_38);
if (sVar2 == 0x20) {
	...
	...
	...
}else {
    puts("The password must be in length of 32!");
}
```
Then it do some shuffle and xor with our input:
```c
local_c = 0;
while (local_c < 0x20) {
  local_68[local_c] = local_38[SHUFFLE[local_c]];
  local_68[local_c] = local_68[local_c] ^ XOR[local_c];
  local_c = local_c + 1;
}
```
For example:
```
If SHUFFLE = [2,0,1]
XOR = [1,2,3]

     shuffle        xor
abc -------->  cab -----> bca

after shuffling become "cab" (3rd,1st,2nd)
after xoring become  "bca" (99 xor 1, 97 xor 2, 98 xor 3)
```
Here comes the tricky part

It check is the output equal to our input:
```c
iVar1 = strncmp((char *)local_68,(char *)local_38,0x20);
```
Then it compare 3 characters with the output. *(Originally it was design to compare 5 characters ("15963"), luckily it still works, sorry about that)*

After that, it print the flag is wgmy{`input`}:
```c
if ((iVar1 == 0) && (iVar1 = strncmp(acStack77,"15963",3), iVar1 == 0)) {
  printf("Correct password! The flag is wgmy{%s}",local_38);
}
```

## Solving

We know the condition of correct input is:
- input == output
- part of input and output is "159"

So how can we find other parts of input?

Look back the process, if output is equal to input:
```
       shuffle                  xor
input --------> shuffled input -----> input

```
Remember how XOR works? 
```
A xor B = C
C xor B = A
C xor A = B
```
So if we know 2 out of the 3 data, we can calculate the left one

We know part of input "159", we can xor it with the `XOR` array, then we found the shuffled input!

Then unshuffle the shuffled input with the SHUFFLE array, then we found a part of the password!

Or you can do the another way round, unshuffle it first then xor it you will get the same result.

Just repeat the steps, until all input is found

If do manually is something like this:
```
???????????????????????????159??

Unshuffle it --> 
```

I solved it with a simple python script:
```py
elf = open("./babyrev",'rb').read()
flag = bytearray(32)
flag[27] = '1'
flag[28] = '5'
flag[29] = '9'
# Get the SHUFFLE and XOR Array from the elf file
SHUFFLE = list(elf[0x3060:0x3080])
XOR = bytearray(elf[0x3080:0x30a0])
# We know 3 input character 
known_char = {
	27:'1',
	28:'5',
	29:'9'
}
# It stops when all the character was found
while not all(flag):
	for i in known_char.keys():
		# Unshuffle it with SHUFFLE array
		index = SHUFFLE.index(chr(i))
		flag[index] = known_char[i]
		del known_char[i]
		# Xor it with XOR array
		flag[index] = flag[index]^XOR[index]
		known_char[index] = flag[index]

print(flag)
```
Result:
```
76420d7abbe073a20436d2fb14b15963
```
Verify the password:
```
./babyrev 
Enter password: 76420d7abbe073a20436d2fb14b15963
Correct password! The flag is wgmy{76420d7abbe073a20436d2fb14b15963}
```
Yes! Challenge solved!

## Flag
> wgmy{76420d7abbe073a20436d2fb14b15963}

## Alternative solution
You can use Z3 Sat Solver, or even Angr to solve this, if you lazy to think about the logic.