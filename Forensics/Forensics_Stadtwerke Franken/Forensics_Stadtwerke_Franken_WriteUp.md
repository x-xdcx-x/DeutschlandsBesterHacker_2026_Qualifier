# Stadtwerke Franken

## Challenge description
```
Freitag, 24. April 2026: 17:42 Uhr. Die IT-Abteilung der Stadtwerke Franken erhält einen Alert ihres EDR-Systems: Auf dem Fileserver SRV- FILE01 wurden innerhalb von 105 Minuten 3,2 Gigabyte Daten in ein unbekanntes lokales Verzeichnis kopiert.

Du wirst als externer DFIR-Analyst hinzugezogen. Deine Aufgabe: Rekonstruiere den vollständigen Angriffspfad: von der ersten verdächtigen Aktivität bis zum Data Staging.
```

## Available artifact
- `PCAP` file: `exfil_dns_tunnel.pcap`

## Solution
The given artifact can be analyzed using `Wireshark`. The capture contains approximately 2,220 packets, all of which were transmitted using the DNS protocol. At first glance, this seems like a large number of packets to analyze manually. However, a large portion of the packets can be actually filtered out during the analysis. These include standard query responses, hostname-related traffic, and packets where the `Info` section repeatedly contains `lbmfqwcy` or `a`, as they do not contain any relevant informations for the analysis. 

To filter out these packets, the following Wireshark display filter can be used: 

```!(dns.flags.response == 1) && dns.qry.type == 16 && !(ip contains "lbmfqwcylbmfqwcy")  && !(ip contains "aaaa")```

Here, `dns.qry.type == 16` filters for `DNS TXT` records. After applying the filter, only 91 packets remain.

They contain obfuscated chunks that are `Base32`-encoded and written in lowercase. Since `Base32` is conventionally represented using uppercase characters, the extracted chunks first have to be converted to uppercase before decoding them. 

After converting and decoding the chunks, the flag was suprisingly found in the very first packet.

```1 ... 000000.emqeiqsipnbdgncdjbptav2bl5kf6tlvgnwgym3sl5gtc3jrnm2hi6s7jq2him3.sgrwh2csylbmfqwcy.c2-frankentransfer.ru```

```bash
┌──(kali㉿xDCx)-[~]
└─$ echo "emqeiqsipnbdgncdjbptav2bl5kf6tlvgnwgym3sl5gtc3jrnm2hi6s7jq2him3sgrwh2csylbmfqwcy" | tr a-z A-Z | base32 -d
# DBH{B34CH_0WA_T_Mu3ll3r_M1m1k4tz_L4t3r4l}
XXXXXX
```

## Flag
```
DBH{B34CH_0WA_T_Mu3ll3r_M1m1k4tz_L4t3r4l}
```
