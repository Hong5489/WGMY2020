# Defuse The Bomb!
Description:
> Never ever try to unzip it!

Attachment:
[bomb.zip](bomb.zip)

We're given a ZIP archive:
```
file bomb.zip 
bomb.zip: Zip archive data, at least v2.0 to extract
```

Run `zipinfo` to see what is inside:
```
zipinfo bomb.zip 
Archive:  bomb.zip
Zip file size: 206803 bytes, number of entries: 20
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 0.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 1.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 10.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 11.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 12.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 13.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 14.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 15.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 16.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 17.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 18.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 19.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 2.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 3.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 4.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 5.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 6.zip
-rw-r--r--  3.0 unx   179640 bx defX 20-Dec-03 13:31 7.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 8.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 9.zip
20 files, 3178638 bytes uncompressed, 204001 bytes compressed:  93.6%
```
You can see there are many zip file compressed inside

Try to unzip 0.zip see whats inside:
```
unzip bomb.zip 0.zip
Archive:  bomb.zip
  inflating: 0.zip                   

zipinfo 0.zip 
Archive:  0.zip
Zip file size: 157842 bytes, number of entries: 20
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 0.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 1.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 10.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 11.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 12.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 13.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 14.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 15.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 16.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 17.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 18.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 19.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 2.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 3.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 4.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 5.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 6.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 7.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 8.zip
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 9.zip
20 files, 2893640 bytes uncompressed, 155040 bytes compressed:  94.7%
```
As you can see, after extract 0.zip, there are more zip to unzip!

If you check for all zip, you will see every zip is contain another 20 other zip file

If you trying to extract, you will find out there are 6 layers of zip files to reach the `flag.txt`

```bash
unzip 0.zip 0.zip
Archive:  0.zip
replace 0.zip? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: 0.zip

unzip 0.zip 0.zip
Archive:  0.zip
replace 0.zip? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: 0.zip   
 ...
 ...
 ...                
caution: filename not matched:  0.zip

ls
0.zip  bomb.zip  README.md

unzip 0.zip 
Archive:  0.zip
  inflating: flag.txt   

```
Then try to grep `wgmy` (Flag format) in `flag.txt`, nothing appear :(

## Solving
To solve this challenge is to find the **biggest zip file in each layer**

Go back to the bomb.zip, if you look closely you will notice a zip file that pop out:
```
zipinfo bomb.zip 
Archive:  bomb.zip
Zip file size: 206803 bytes, number of entries: 20
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 0.zip
...
...
-rw-r--r--  3.0 unx   179640 bx defX 20-Dec-03 13:31 7.zip <--
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 8.zip
-rw-r--r--  3.0 unx   157842 bx defX 20-Dec-03 13:31 9.zip
20 files, 3178638 bytes uncompressed, 204001 bytes compressed:  93.6%
```
As you can see, the `7.zip` is the biggest zip file!

Then unzip it, and find another biggest zip file:
```bash
unzip bomb.zip 7.zip
Archive:  bomb.zip
  inflating: 7.zip                   
zipinfo 7.zip 
Archive:  7.zip
Zip file size: 179640 bytes, number of entries: 20
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 0.zip
-rw-r--r--  3.0 unx   160095 bx defX 20-Dec-03 13:31 1.zip <--
...
...
-rw-r--r--  3.0 unx   144682 bx defX 20-Dec-03 13:31 9.zip
20 files, 2909053 bytes uncompressed, 176838 bytes compressed:  93.9%
```
This time is `1.zip`

Then repeat the steps until it reach the last layer of zip, which contain the `flag.txt`

```bash
unzip bomb.zip 7.zip
unzip 7.zip 1.zip
unzip 1.zip 4.zip
unzip 4.zip 9.zip
unzip 9.zip 18.zip
unzip 18.zip 8.zip
zipinfo 8.zip 
Archive:  8.zip
Zip file size: 2089372 bytes, number of entries: 1
-rw-r--r--  3.0 unx 2147485734 tx defX 20-Dec-03 13:30 flag.txt
1 file, 2147485734 bytes uncompressed, 2089206 bytes compressed:  99.9%

unzip 8.zip 
Archive:  8.zip
replace flag.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: y
  inflating: flag.txt                
```
Then grep the flag!
```bash
grep wgmy flag.txt 
wgmy{04a2766e72f0e267ed58792cc1579791}
```
Thats it! Easy challenge!

## Flag 
> wgmy{04a2766e72f0e267ed58792cc1579791}

## Small note
This challenge is actually a [zip bomb](https://en.wikipedia.org/wiki/Zip_bomb) that will make your hardisk explode!