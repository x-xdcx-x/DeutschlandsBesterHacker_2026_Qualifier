# Lost Developer

## Challenge description
```
Alex Carter ist Softwareentwickler und Fotograf. Vor einiger Zeit ist er aus der Oeffentlichkeit verschwunden. Zurueck blieben verstreute Spuren seiner Arbeit: Projekte, Bilder, Dokumente, Fragmente aus verschiedenen Phasen seines Lebens.

Auf den ersten Blick gehoert nichts davon zusammen. Aber irgendwo dazwischen hat Alex etwas hinterlassen. Etwas, das offenbar nicht fuer alle bestimmt war. Finde es.
```

## Link to the challenge
- https://lost-developer-02506f2f1c97d533.dbhchallenge.de

The website represents a homepage about Alex Carters profile. It contains a short decription about him and his hobby, contact informations, his connection platforms and his blogs.

## Solution
First let's take a look on `About Me` (link: https://lost-developer-02506f2f1c97d533.dbhchallenge.de/about.html). There, a `resume.pdf` can be found. Let's download and analyze it with `exiftool` to get a brief information about the file:

```bash
┌──(kali㉿xDCx)-[~]
└─$ exiftool resume.pdf

ExifTool Version Number         : 13.55
File Name                       : resume.pdf
Directory                       : .
File Size                       : 5.6 kB
File Modification Date/Time     : 2026:08:11 20:14:02+02:00
File Access Date/Time           : 2026:08:17 18:54:24+02:00
File Inode Change Date/Time     : 2026:08:17 18:54:18+02:00
File Permissions                : -rw-r--r--
File Type                       : PDF
File Type Extension             : pdf
MIME Type                       : application/pdf
PDF Version                     : 1.3
Linearized                      : No
Create Date                     : 2026:08:11 14:14:01-04:00
Creator                         : anonymous
Keywords                        : flag_location=/hiddden/, crypto=id_rsa.pub
Modify Date                     : 2026:08:11 14:14:01-04:00
Producer                        : ReportLab PDF Library - (opensource)
Trapped                         : False
Page Mode                       : UseNone
Page Count                      : 1
XMP Toolkit                     : Image::ExifTool 13.55
Subject                         : Old development document
Title                           : Developer Portfolio
Author                          : Alex Carter
```
The result shows a lot of basic informations about the file, but there is one particular section that seems to be interesting: `Keywords: flag_location=/hiddden/, crypto=id_rsa.pub`. Since this is the first hint in the challenge, let's keep that in mind and get back to it later once more informations have been found.

In `Blog` (link: https://lost-developer-81b496df1ab65cf5.dbhchallenge.de/blog.html) another hint was found. Especially the blog about `Photography Backup Workflow`, where he wrote: `Keeping personal files organized is important. I created a small archive system for my photos and documents. Old projects are sometimes still accessible during development.`. Since `resume.pdf` was already found, this might me a hint that more files like that exist and can be downloaded as well as analyzed. 

Also another hint that strengthens the approach to look at his photos and documents was found in `Contact` (link: https://lost-developer-81b496df1ab65cf5.dbhchallenge.de/contact.html), to be specific, in the source code of this site there is a comment that says: `<!-- Temporary developer note: Website migration completed. Check old backup files before removing. -->`. 

On his GitHub profile (link: https://lost-developer-81b496df1ab65cf5.dbhchallenge.de/social/github.html) two files that can be found as his projects. One is called `portfolio` and the other one is called `photo-manager`. Looking at the source code another comment can be detected: `<!-- Repository note: Main project: portfolio, Important file: projecthint.jpg --> `. That means the file `projecthint.jpg` can be found on `portfolio`. After clicking on `View project` the content of the image says: `Look deep INSIDE me...` which is an indicator to analyze it. (From this point, all pages from the site were discovered fully and there were no other photos or documents that can be downloaded anymore. The other image that was found on `photo-manager` did not reveal much informations that can help, therefore it got skipped.)

```bash
┌──(kali㉿xDCx)-\[\~]
└─$ exiftool projecthint.jpg

ExifTool Version Number         : 13.55
File Name                       : projecthint.jpg
Directory                       : .
File Size                       : 51 kB
File Modification Date/Time     : 2026:08:11 20:14:01+02:00
File Access Date/Time           : 2026:08:17 18:16:10+02:00
File Inode Change Date/Time     : 2026:08:17 18:15:57+02:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 1
Y Resolution                    : 1
Resolution Unit                 : None
Software                        : Photo Manager v1.4
Artist                          : lostdev
Y Cb Cr Positioning             : Centered
XMP Toolkit                     : Image::ExifTool 13.55
Description                     : Mountain trip archive
Author                          : Alex Carter
Comment                         : wget me check me and find hidden places
Image Width                     : 1600
Image Height                    : 900
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 1600x900
Megapixels                      : 1.4
```

The image provides one crucial information in the section `Comment`: `wget me check me and find hidden places`. On the first glance it might be confusing since all pages and source codes were discovered. But let's remember the result from `resume.pdf` again, where two informations were found: `flag_location=/hiddden/` and `crypto=id_rsa.pub`. The information found on `projecthint.jpg` just referred to this document.

The flag location looks like a directory that can be visited with the provided link. When doing that, a `403 Forbidden` was shown. That means it needs to be accessed in a **authorized** way. Putting this aside, let's see if the website has in general any other files or directories:

```bash
┌──(kali㉿xDCx)-\[\~]
└─$ ffuf -u https://lost-developer-81b496df1ab65cf5.dbhchallenge.de/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt


        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 Method           : GET
 URL              : https://lost-developer-81b496df1ab65cf5.dbhchallenge.de/FUZZ
 Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt
 Follow redirects : false
 Calibration      : false
 Timeout          : 10
 Threads          : 40
 Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

index.html              [Status: 200, Size: 2374, Words: 475, Lines: 247, Duration: 22ms]
contact.html            [Status: 200, Size: 1941, Words: 314, Lines: 224, Duration: 23ms]
robots.txt              [Status: 200, Size: 128, Words: 13, Lines: 11, Duration: 20ms]
.                       [Status: 200, Size: 2374, Words: 475, Lines: 247, Duration: 20ms]
about.html              [Status: 200, Size: 2804, Words: 801, Lines: 277, Duration: 19ms]
blog.html               [Status: 200, Size: 1948, Words: 347, Lines: 201, Duration: 19ms]
:: Progress: [17129/17129] :: Job [1/1] :: 1739 req/sec :: Duration: [0:00:09] :: Errors: 0 ::
```

Among all the pages that have been already visited, the `robots.txt` was left untouched. Reading `robots.txt` it reveals:
```
User-agent: \*

# I have nice Projects
# Disallow: /exifisathing/

# Sitemap temporarily disabled
# sitemap: /old/sitemap.xml
```

Neither `exifisathing` nor `old` was accessible since they only returns `404 Not Found`, which means they don't exist at all. Now lets move on with directories:

```bash
┌──(kali㉿xDCx)-[~]
└─$ ffuf -u https://lost-developer-21934f50f4008341.dbhchallenge.de/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://lost-developer-21934f50f4008341.dbhchallenge.de/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

assets                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 21ms]
social                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 20ms]
check                   [Status: 403, Size: 6, Words: 1, Lines: 1, Duration: 25ms]
unlock                  [Status: 403, Size: 13, Words: 2, Lines: 1, Duration: 21ms]
:: Progress: [26583/26583] :: Job [1/1] :: 324 req/sec :: Duration: [0:00:16] :: Errors: 1 ::
```

It seems like 2 new directories were discovered. `check` and `unlock` have both the status code `403` which is `Forbidden`. When visiting, `check` returns `LOCKED` whereas `unlock` returns `Invalid token`. To sum up, `unlock` might be the key to access `hiddden` after providing it with the right token and `check` might only check if the `hiddden` is still locked or not. Since both do not have any subdirectories let's check `assets`.

```bash
┌──(kali㉿xDCx)-[~]
└─$ ffuf -u https://lost-developer-21934f50f4008341.dbhchallenge.de/assets/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://lost-developer-21934f50f4008341.dbhchallenge.de/assets/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-large-directories-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

css                     [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 22ms]
img                     [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 20ms]
pdf                     [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 21ms]
crypto                  [Status: 301, Size: 162, Words: 5, Lines: 8, Duration: 21ms]
:: Progress: [56162/56162] :: Job [1/1] :: 1886 req/sec :: Duration: [0:00:33] :: Errors: 0 ::
```

the result is pretty clear. There is a directory called `crypto`, the same name as mentioned in `resume.pdf`. That can only mean that behind it there is `id_rsa.pub`.

```bash
┌──(kali㉿xDCx)-[~]
└─$ ffuf -u https://lost-developer-21934f50f4008341.dbhchallenge.de/assets/crypto/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://lost-developer-21934f50f4008341.dbhchallenge.de/assets/crypto/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

id_rsa.pub              [Status: 200, Size: 97, Words: 7, Lines: 4, Duration: 28ms]
secret                  [Status: 200, Size: 45, Words: 2, Lines: 2, Duration: 20ms]
:: Progress: [4746/4746] :: Job [1/1] :: 1739 req/sec :: Duration: [0:00:03] :: Errors: 0 ::
```

Not only the public key is found there but also a file called `secret`. After downloaded both and read the contents of both files, it is clear that `secret` contains the ciphertext and `id_rsa.pub` obviously the public key:
```bash
┌──(kali㉿xDCx)-[~/Lost Developer]
└─$ cat secret
Ciphertext: 2655eacc028dfa8924e8223e39fad4b3

┌──(kali㉿xDCx)-[~/Lost Developer]
└─$ cat id_rsa.pub
-----BEGIN RSA PUBLIC KEY-----
MBgCEQCeyf5W0WFpCSE7+2NzKY7vAgMBAAE=
-----END RSA PUBLIC KEY-----
```
But looking at the length of that key, it seems to be too short to be a strong encryption. A deeper analysis reveals that the key is only 128 bit.

```bash
┌──(kali㉿xDCx)-[~/Lost Developer]
└─$ openssl rsa -RSAPublicKey_in -in id_rsa.pub -text -noout
Public-Key: (128 bit)
Modulus:
    00:9e:c9:fe:56:d1:61:69:09:21:3b:fb:63:73:29:
    8e:ef
Exponent: 65537 (0x10001)
```
Since RSA 128 bit is pretty much deprecated. The private key can be recovered. A small program was made that recovers the private key and decrypts the ciphertext (see: [recover_decrypt_rsa.py](recover_decrypt_rsa.py)). 

After executing the program the plaintext is:
```bash
┌──(kali㉿xDCx)-[~]
└─$ python3 decrev.py
Plaintext: UNLOCK-7F3A9C2D
```
Since it has the prefix `UNLOCK` it is likely the token to the directory `/unlock`. To include this token, add the parameter `token=` with the decrypted token as the value behind the directory as here: `https://lost-developer-21934f50f4008341.dbhchallenge.de/unlock?token=UNLOCK-7F3A9C2D`

By visiting it, instead of `Invalid token` it now shows:
```
Archive unlocked
Access granted.

Continue to archive
```
`archive` is marked as a link. The link leads to the `/hiddden` directory:

```
Index of /hiddden/
../
draft.html                                         01-Aug-2026 15:28                 630
flag.txt                                           26-Aug-2026 05:43                  45
notes.html                                         11-Aug-2026 17:59                 331
```
And there is the flag file!

- `draft.html`
```
Website Migration Draft
This page is currently not ready.

The new portfolio design is almost finished.

Developer Notes
Update project descriptions
Replace old images
Remove temporary files
Last updated: January 2026
```

- `notes.html`
```
Old Developer Notes
The old archive is finally cleaned up.

One last thing remained encoded:

VGhlIGZsYWcgaXM6IERCSHszWDFGXzJfUjVBXzJfRkw0R18wV04zRH0=
```
The base64 encoded string decoded to: `DBH{3X1F_2_R5A_2_FL4G_0WN3D}`. But it is not the real flag. The real one can be found in `flag.txt`

- `flag.txt`
```
DBH{3X1F_2_R5A_2_FL4G_0WN3D_21934f50f4008341}
```

## Flag
```
DBH{3X1F_2_R5A_2_FL4G_0WN3D_21934f50f4008341}
```