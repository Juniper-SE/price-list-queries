# price-list-queries
A simple Python script to search for SKU information in an juniper price list excel file.  

Place the pricelist_2023_03.xlsx file in the same directory as the script.

- Enter the name of the product when prompted.
- If an exact match is found, enter the quantity of the product when prompted.
- The script will display the product information and total price in a table format.
- If an exact match is not found, the script will suggest similar products


examples:
<pre>

Enter the name of the product: ex2300-24p
Enter the quantity of the product: 1
+----------------+----------+-------------+------------+-----+------------+---------+--------+
| Product Number | Quantity | Total Price | List Price | LOD |    ADD     | EOL Rep | Status |
+----------------+----------+-------------+------------+-----+------------+---------+--------+
|   EX2300-24P   |    1     |     2993    |    2993    | NaT | 2016-04-01 |   nan   |  Ship  |
+----------------+----------+-------------+------------+-----+------------+---------+--------+
EX2300 24-port 10/100/1000BaseT PoE+, 4 x 1/10G SFP/SFP+ (optics sold separately)


Enter the name of the product: ex4300-48p
Enter the quantity of the product: 2
+----------------+----------+-------------+------------+------------+------------+------------+--------+
| Product Number | Quantity | Total Price | List Price |    LOD     |    ADD     |  EOL Rep   | Status |
+----------------+----------+-------------+------------+------------+------------+------------+--------+
|   EX4300-48P   |    2     |    27000    |   13500    | 2023-06-30 | 2013-08-02 | EX4400-48P |  Ship  |
+----------------+----------+-------------+------------+------------+------------+------------+--------+
EX4300, 48-Port 10/100/1000BaseT PoE-plus + 1100W AC PS


Enter the name of the product: mx150
Enter the quantity of the product: 3
+----------------+----------+-------------+------------+------------+------------+----------------+--------+
| Product Number | Quantity | Total Price | List Price |    LOD     |    ADD     |    EOL Rep     | Status |
+----------------+----------+-------------+------------+------------+------------+----------------+--------+
|     MX150      |    3     |    59850    |   19950    | 2023-06-30 | 2017-10-06 | No Replacement |  Ship  |
+----------------+----------+-------------+------------+------------+------------+----------------+--------+
MX150 router appliance. That has 12x1G and 2x10G ports, maximum throughput is 20G


Enter the name of the product: ACX7024-DC-2PSU-L
Enter the quantity of the product: 4
+-------------------+----------+-------------+------------+-----+------------+---------+----------------------+
|   Product Number  | Quantity | Total Price | List Price | LOD |    ADD     | EOL Rep |        Status        |
+-------------------+----------+-------------+------------+-----+------------+---------+----------------------+
| ACX7024-DC-2PSU-L |    4     |    112000   |   28000    | NaT | 2022-12-02 |   nan   | Avail. to Order (PP) |
+-------------------+----------+-------------+------------+-----+------------+---------+----------------------+
ACX7024, 1RU high, 250mm deep; 24xSFP28 and 4xQSFP28-DD; Operating Range 40C to 65C; DC Redundant Power Supply Unit; Limited Junos


Enter the name of the product: ssr
Did you mean:
S-ES
SSR120
SSR1200
SSR130
SSR1300
SSR1400
SSR1500
Please check again.
ssr not found in any sheet.
Enter the name of the product: ap12
Did you mean:
AP12-US
AP12-WW
APBRU-T12
Please check again.
ap12 not found in any sheet.
Enter the name of the product: mx204
Did you mean:
EX9204-ML
MX104-AC
MX104-DC
MX104-T
MX150
MX204-HW-BASE
S-MX104-Q
VMX-250M
Please check again.
mx204 not found in any sheet.
Enter the name of the product: MX204-HW-BASE
Enter the quantity of the product: 6
+----------------+----------+-------------+------------+-----+------------+--------------------+--------+
| Product Number | Quantity | Total Price | List Price | LOD |    ADD     |      EOL Rep       | Status |
+----------------+----------+-------------+------------+-----+------------+--------------------+--------+
| MX204-HW-BASE  |    6     |    225000   |   37500    | NaT | 2020-04-03 | MX304, ACX7100-48L |  Ship  |
+----------------+----------+-------------+------------+-----+------------+--------------------+--------+
MX204 Integrated SKU with Base HW + Standard Junos SW, Perpetual

</pre>
