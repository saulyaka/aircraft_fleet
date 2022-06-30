# Generated by Django 3.2.13 on 2022-06-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_airport',
            field=models.CharField(choices=[('AG', 'Solomon Islands'), ('AN', 'Nauru'), ('AY', 'Papua New Guinea'), ('BG', 'Greenland'), ('BI', 'Iceland'), ('BK', 'Kosovo'), ('C', 'Canada'), ('DA', 'Algeria'), ('DB', 'Benin'), ('DF', 'Burkina Faso'), ('DG', 'Ghana'), ('DI', "Côte d'Ivoire"), ('DN', 'Nigeria'), ('DR', 'Niger'), ('DT', 'Tunisia'), ('DX', 'Togo'), ('EB', 'Belgium'), ('ED', 'Germany (civil)'), ('EE', 'Estonia'), ('EF', 'Finland'), ('EG', 'United Kingdom (and Crown Dependencies)'), ('EH', 'Netherlands'), ('EI', 'Ireland'), ('EK', 'Denmark and the Faroe Islands'), ('EL', 'Luxembourg'), ('EN', 'Norway'), ('EP', 'Poland'), ('ES', 'Sweden'), ('ET', 'Germany (military)'), ('EV', 'Latvia'), ('EY', 'Lithuania'), ('FA', 'South Africa'), ('FB', 'Botswana'), ('FC', 'Republic of the Congo'), ('FD', 'Eswatini'), ('FE', 'Central African Republic'), ('FG', 'Equatorial Guinea'), ('FH', 'Saint Helena, Ascension and Tristan da Cunha'), ('FI', 'Mauritius'), ('FJ', 'British Indian Ocean Territory'), ('FK', 'Cameroon'), ('FL', 'Zambia'), ('FM', 'Comoros, France (Mayotte and Réunion), and Madagascar'), ('FN', 'Angola'), ('FO', 'Gabon'), ('FP', 'São Tomé and Príncipe'), ('FQ', 'Mozambique'), ('FS', 'Seychelles'), ('FT', 'Chad'), ('FV', 'Zimbabwe'), ('FW', 'Malawi'), ('FX', 'Lesotho'), ('FY', 'Namibia'), ('FZ', 'Democratic Republic of the Congo'), ('GA', 'Mali'), ('GB', 'The Gambia'), ('GC', 'Spain (Canary Islands)'), ('GE', 'Spain (Ceuta and Melilla)'), ('GF', 'Sierra Leone'), ('GG', 'Guinea-Bissau'), ('GL', 'Liberia'), ('GM', 'Morocco'), ('GO', 'Senegal'), ('GQ', 'Mauritania'), ('GS', 'Western Sahara'), ('GU', 'Guinea'), ('GV', 'Cape Verde'), ('HA', 'Ethiopia'), ('HB', 'Burundi'), ('HC', 'Somalia (including Somaliland)'), ('HD', 'Djibouti'), ('HE', 'Egypt'), ('HH', 'Eritrea'), ('HJ', 'South Sudan'), ('HK', 'Kenya'), ('HL', 'Libya'), ('HR', 'Rwanda'), ('HS', 'Sudan'), ('HT', 'Tanzania'), ('HU', 'Uganda'), ('K', 'Contiguous United States'), ('LA', 'Albania'), ('LB', 'Bulgaria'), ('LC', 'Cyprus'), ('LD', 'Croatia'), ('LE', 'Spain (mainland section and Balearic Islands)'), ('LF', 'France (Metropolitan France; including Saint-Pierre and Miquelon)'), ('LG', 'Greece'), ('LH', 'Hungary'), ('LI', 'Italy (and San Marino)'), ('LJ', 'Slovenia'), ('LK', 'Czech Republic'), ('LL', 'Israel'), ('LM', 'Malta'), ('LN', 'Monaco'), ('LO', 'Austria'), ('LP', 'Portugal (including the Azores and Madeira)'), ('LQ', 'Bosnia and Herzegovina'), ('LR', 'Romania'), ('LS', 'Switzerland'), ('LT', 'Turkey'), ('LU', 'Moldova'), ('LV', 'Palestine/Palestinian territories'), ('LW', 'North Macedonia'), ('LX', 'Gibraltar'), ('LY', 'Serbia and Montenegro'), ('LZ', 'Slovakia'), ('MB', 'Turks and Caicos Islands'), ('MD', 'Dominican Republic'), ('MG', 'Guatemala'), ('MH', 'Honduras'), ('MK', 'Jamaica'), ('MM', 'Mexico'), ('MN', 'Nicaragua'), ('MP', 'Panama'), ('MR', 'Costa Rica'), ('MS', 'El Salvador'), ('MT', 'Haiti'), ('MU', 'Cuba'), ('MW', 'Cayman Islands'), ('MY', 'Bahamas'), ('MZ', 'Belize'), ('NC', 'Cook Islands'), ('NF', 'Fiji, Tonga'), ('NG', 'Kiribati (Gilbert Islands), Tuvalu'), ('NI', 'Niue'), ('NL', 'France (Wallis and Futuna)'), ('NS', 'Samoa, United States (American Samoa)'), ('NT', 'France (French Polynesia)'), ('NV', 'Vanuatu'), ('NW', 'France (New Caledonia)'), ('NZ', 'New Zealand, parts of Antarctica'), ('OA', 'Afghanistan'), ('OB', 'Bahrain'), ('OE', 'Saudi Arabia'), ('OI', 'Iran'), ('OJ', 'Jordan and the West Bank'), ('OK', 'Kuwait'), ('OL', 'Lebanon'), ('OM', 'United Arab Emirates'), ('OO', 'Oman'), ('OP', 'Pakistan'), ('OR', 'Iraq'), ('OS', 'Syria'), ('OT', 'Qatar'), ('OY', 'Yemen'), ('PA', 'US (Alaska) (also PF, PO and PP)'), ('PB', 'US (Baker Island)'), ('PC', 'Kiribati (Canton Airfield, Phoenix Islands)'), ('PF', 'US (Alaska) (also PA, PO and PP)'), ('PG', 'US (Guam, Northern Mariana Islands)'), ('PH', 'US (Hawaii)'), ('PJ', 'US (Johnston Atoll)'), ('PK', 'Marshall Islands'), ('PL', 'Kiribati (Line Islands)'), ('PM', 'US (Midway Island)'), ('PO', 'US (Alaska) (also PA, PF and PP)'), ('PP', 'US (Alaska) (also PA, PF and PO)'), ('PT', 'Federated States of Micronesia, Palau'), ('PW', 'US (Wake Island)'), ('RC', 'Republic of China (Taiwan)'), ('RJ', 'Japan (Mainland)'), ('RK', 'South Korea (Republic of Korea)'), ('RO', 'Japan (Okinawa)'), ('RP', 'Philippines'), ('SA', 'Argentina (including parts of Antarctica)'), ('SB', 'Brazil (also SD, SI, SJ, SN, SS and SW)'), ('SC', 'Chile (including Easter Island and parts of Antarctica) (also SH)'), ('SD', 'Brazil (also SB, SI, SJ, SN, SS and SW)'), ('SE', 'Ecuador'), ('SF', 'United Kingdom (Falkland Islands)'), ('SG', 'Paraguay'), ('SH', 'Chile (also SC)'), ('SI', 'Brazil (also SB, SD, SJ, SN, SS and SW)'), ('SJ', 'Brazil (also SB, SD, SI, SN, SS and SW)'), ('SK', 'Colombia'), ('SL', 'Bolivia'), ('SM', 'Suriname'), ('SN', 'Brazil (also SB, SD, SI, SJ, SS and SW)'), ('SO', 'France (French Guiana)'), ('SP', 'Peru'), ('SS', 'Brazil (also SB, SD, SI, SJ, SN and SW)'), ('SU', 'Uruguay'), ('SV', 'Venezuela'), ('SW', 'Brazil (also SB, SD, SI, SJ, SN and SS)'), ('SY', 'Guyana'), ('TA', 'Antigua and Barbuda'), ('TB', 'Barbados'), ('TD', 'Dominica'), ('TF', 'France (Guadeloupe, Martinique, Saint Barthélemy, Saint Martin)'), ('TG', 'Grenada'), ('TI', 'US (U.S. Virgin Islands)'), ('TJ', 'US (Puerto Rico)'), ('TK', 'Saint Kitts and Nevis'), ('TL', 'Saint Lucia'), ('TN', 'Caribbean Netherlands, Aruba, Curaçao, Sint Maarten'), ('TQ', 'UK (Anguilla)'), ('TR', 'UK (Montserrat)'), ('TT', 'Trinidad and Tobago'), ('TU', 'UK (British Virgin Islands)'), ('TV', 'Saint Vincent and the Grenadines'), ('TX', 'UK (Bermuda)'), ('U', 'Russia (except as below)'), ('UA', 'Kazakhstan'), ('UB', 'Azerbaijan'), ('UC', 'Kyrgyzstan'), ('UD', 'Armenia'), ('UG', 'Georgia'), ('UK', 'Ukraine'), ('UM', 'Belarus and Russia (Kaliningrad Oblast)'), ('UT', 'Tajikistan, Turkmenistan, Uzbekistan'), ('VA', 'India (West India)'), ('VC', 'Sri Lanka'), ('VD', 'Cambodia'), ('VE', 'India (East India)'), ('VG', 'Bangladesh'), ('VH', 'Hong Kong'), ('VI', 'India (North India)'), ('VL', 'Laos'), ('VM', 'Macau'), ('VN', 'Nepal'), ('VO', 'India (South India)'), ('VQ', 'Bhutan'), ('VR', 'Maldives'), ('VT', 'Thailand'), ('VV', 'Vietnam'), ('VY', 'Myanmar'), ('WA', 'Indonesia (also WI, WQ and WR)'), ('WB', 'Brunei, Malaysia (East Malaysia)'), ('WI', 'Indonesia (also WA, WQ and WR)'), ('WM', 'Malaysia (Peninsular Malaysia)'), ('WP', 'Timor-Leste'), ('WQ', 'Indonesia (also WA, WI and WR)'), ('WR', 'Indonesia (also WA, WI and WQ)'), ('WS', 'Singapore'), ('Y', 'Australia (including Norfolk Island, Christmas Island, Cocos (Keeling) Islands and Australian Antarctic Territory)'), ('Z', 'Mainland China (except ZK and ZM)'), ('ZK', 'North Korea'), ('ZM', 'Mongolia')], max_length=2),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_airport',
            field=models.CharField(choices=[('AG', 'Solomon Islands'), ('AN', 'Nauru'), ('AY', 'Papua New Guinea'), ('BG', 'Greenland'), ('BI', 'Iceland'), ('BK', 'Kosovo'), ('C', 'Canada'), ('DA', 'Algeria'), ('DB', 'Benin'), ('DF', 'Burkina Faso'), ('DG', 'Ghana'), ('DI', "Côte d'Ivoire"), ('DN', 'Nigeria'), ('DR', 'Niger'), ('DT', 'Tunisia'), ('DX', 'Togo'), ('EB', 'Belgium'), ('ED', 'Germany (civil)'), ('EE', 'Estonia'), ('EF', 'Finland'), ('EG', 'United Kingdom (and Crown Dependencies)'), ('EH', 'Netherlands'), ('EI', 'Ireland'), ('EK', 'Denmark and the Faroe Islands'), ('EL', 'Luxembourg'), ('EN', 'Norway'), ('EP', 'Poland'), ('ES', 'Sweden'), ('ET', 'Germany (military)'), ('EV', 'Latvia'), ('EY', 'Lithuania'), ('FA', 'South Africa'), ('FB', 'Botswana'), ('FC', 'Republic of the Congo'), ('FD', 'Eswatini'), ('FE', 'Central African Republic'), ('FG', 'Equatorial Guinea'), ('FH', 'Saint Helena, Ascension and Tristan da Cunha'), ('FI', 'Mauritius'), ('FJ', 'British Indian Ocean Territory'), ('FK', 'Cameroon'), ('FL', 'Zambia'), ('FM', 'Comoros, France (Mayotte and Réunion), and Madagascar'), ('FN', 'Angola'), ('FO', 'Gabon'), ('FP', 'São Tomé and Príncipe'), ('FQ', 'Mozambique'), ('FS', 'Seychelles'), ('FT', 'Chad'), ('FV', 'Zimbabwe'), ('FW', 'Malawi'), ('FX', 'Lesotho'), ('FY', 'Namibia'), ('FZ', 'Democratic Republic of the Congo'), ('GA', 'Mali'), ('GB', 'The Gambia'), ('GC', 'Spain (Canary Islands)'), ('GE', 'Spain (Ceuta and Melilla)'), ('GF', 'Sierra Leone'), ('GG', 'Guinea-Bissau'), ('GL', 'Liberia'), ('GM', 'Morocco'), ('GO', 'Senegal'), ('GQ', 'Mauritania'), ('GS', 'Western Sahara'), ('GU', 'Guinea'), ('GV', 'Cape Verde'), ('HA', 'Ethiopia'), ('HB', 'Burundi'), ('HC', 'Somalia (including Somaliland)'), ('HD', 'Djibouti'), ('HE', 'Egypt'), ('HH', 'Eritrea'), ('HJ', 'South Sudan'), ('HK', 'Kenya'), ('HL', 'Libya'), ('HR', 'Rwanda'), ('HS', 'Sudan'), ('HT', 'Tanzania'), ('HU', 'Uganda'), ('K', 'Contiguous United States'), ('LA', 'Albania'), ('LB', 'Bulgaria'), ('LC', 'Cyprus'), ('LD', 'Croatia'), ('LE', 'Spain (mainland section and Balearic Islands)'), ('LF', 'France (Metropolitan France; including Saint-Pierre and Miquelon)'), ('LG', 'Greece'), ('LH', 'Hungary'), ('LI', 'Italy (and San Marino)'), ('LJ', 'Slovenia'), ('LK', 'Czech Republic'), ('LL', 'Israel'), ('LM', 'Malta'), ('LN', 'Monaco'), ('LO', 'Austria'), ('LP', 'Portugal (including the Azores and Madeira)'), ('LQ', 'Bosnia and Herzegovina'), ('LR', 'Romania'), ('LS', 'Switzerland'), ('LT', 'Turkey'), ('LU', 'Moldova'), ('LV', 'Palestine/Palestinian territories'), ('LW', 'North Macedonia'), ('LX', 'Gibraltar'), ('LY', 'Serbia and Montenegro'), ('LZ', 'Slovakia'), ('MB', 'Turks and Caicos Islands'), ('MD', 'Dominican Republic'), ('MG', 'Guatemala'), ('MH', 'Honduras'), ('MK', 'Jamaica'), ('MM', 'Mexico'), ('MN', 'Nicaragua'), ('MP', 'Panama'), ('MR', 'Costa Rica'), ('MS', 'El Salvador'), ('MT', 'Haiti'), ('MU', 'Cuba'), ('MW', 'Cayman Islands'), ('MY', 'Bahamas'), ('MZ', 'Belize'), ('NC', 'Cook Islands'), ('NF', 'Fiji, Tonga'), ('NG', 'Kiribati (Gilbert Islands), Tuvalu'), ('NI', 'Niue'), ('NL', 'France (Wallis and Futuna)'), ('NS', 'Samoa, United States (American Samoa)'), ('NT', 'France (French Polynesia)'), ('NV', 'Vanuatu'), ('NW', 'France (New Caledonia)'), ('NZ', 'New Zealand, parts of Antarctica'), ('OA', 'Afghanistan'), ('OB', 'Bahrain'), ('OE', 'Saudi Arabia'), ('OI', 'Iran'), ('OJ', 'Jordan and the West Bank'), ('OK', 'Kuwait'), ('OL', 'Lebanon'), ('OM', 'United Arab Emirates'), ('OO', 'Oman'), ('OP', 'Pakistan'), ('OR', 'Iraq'), ('OS', 'Syria'), ('OT', 'Qatar'), ('OY', 'Yemen'), ('PA', 'US (Alaska) (also PF, PO and PP)'), ('PB', 'US (Baker Island)'), ('PC', 'Kiribati (Canton Airfield, Phoenix Islands)'), ('PF', 'US (Alaska) (also PA, PO and PP)'), ('PG', 'US (Guam, Northern Mariana Islands)'), ('PH', 'US (Hawaii)'), ('PJ', 'US (Johnston Atoll)'), ('PK', 'Marshall Islands'), ('PL', 'Kiribati (Line Islands)'), ('PM', 'US (Midway Island)'), ('PO', 'US (Alaska) (also PA, PF and PP)'), ('PP', 'US (Alaska) (also PA, PF and PO)'), ('PT', 'Federated States of Micronesia, Palau'), ('PW', 'US (Wake Island)'), ('RC', 'Republic of China (Taiwan)'), ('RJ', 'Japan (Mainland)'), ('RK', 'South Korea (Republic of Korea)'), ('RO', 'Japan (Okinawa)'), ('RP', 'Philippines'), ('SA', 'Argentina (including parts of Antarctica)'), ('SB', 'Brazil (also SD, SI, SJ, SN, SS and SW)'), ('SC', 'Chile (including Easter Island and parts of Antarctica) (also SH)'), ('SD', 'Brazil (also SB, SI, SJ, SN, SS and SW)'), ('SE', 'Ecuador'), ('SF', 'United Kingdom (Falkland Islands)'), ('SG', 'Paraguay'), ('SH', 'Chile (also SC)'), ('SI', 'Brazil (also SB, SD, SJ, SN, SS and SW)'), ('SJ', 'Brazil (also SB, SD, SI, SN, SS and SW)'), ('SK', 'Colombia'), ('SL', 'Bolivia'), ('SM', 'Suriname'), ('SN', 'Brazil (also SB, SD, SI, SJ, SS and SW)'), ('SO', 'France (French Guiana)'), ('SP', 'Peru'), ('SS', 'Brazil (also SB, SD, SI, SJ, SN and SW)'), ('SU', 'Uruguay'), ('SV', 'Venezuela'), ('SW', 'Brazil (also SB, SD, SI, SJ, SN and SS)'), ('SY', 'Guyana'), ('TA', 'Antigua and Barbuda'), ('TB', 'Barbados'), ('TD', 'Dominica'), ('TF', 'France (Guadeloupe, Martinique, Saint Barthélemy, Saint Martin)'), ('TG', 'Grenada'), ('TI', 'US (U.S. Virgin Islands)'), ('TJ', 'US (Puerto Rico)'), ('TK', 'Saint Kitts and Nevis'), ('TL', 'Saint Lucia'), ('TN', 'Caribbean Netherlands, Aruba, Curaçao, Sint Maarten'), ('TQ', 'UK (Anguilla)'), ('TR', 'UK (Montserrat)'), ('TT', 'Trinidad and Tobago'), ('TU', 'UK (British Virgin Islands)'), ('TV', 'Saint Vincent and the Grenadines'), ('TX', 'UK (Bermuda)'), ('U', 'Russia (except as below)'), ('UA', 'Kazakhstan'), ('UB', 'Azerbaijan'), ('UC', 'Kyrgyzstan'), ('UD', 'Armenia'), ('UG', 'Georgia'), ('UK', 'Ukraine'), ('UM', 'Belarus and Russia (Kaliningrad Oblast)'), ('UT', 'Tajikistan, Turkmenistan, Uzbekistan'), ('VA', 'India (West India)'), ('VC', 'Sri Lanka'), ('VD', 'Cambodia'), ('VE', 'India (East India)'), ('VG', 'Bangladesh'), ('VH', 'Hong Kong'), ('VI', 'India (North India)'), ('VL', 'Laos'), ('VM', 'Macau'), ('VN', 'Nepal'), ('VO', 'India (South India)'), ('VQ', 'Bhutan'), ('VR', 'Maldives'), ('VT', 'Thailand'), ('VV', 'Vietnam'), ('VY', 'Myanmar'), ('WA', 'Indonesia (also WI, WQ and WR)'), ('WB', 'Brunei, Malaysia (East Malaysia)'), ('WI', 'Indonesia (also WA, WQ and WR)'), ('WM', 'Malaysia (Peninsular Malaysia)'), ('WP', 'Timor-Leste'), ('WQ', 'Indonesia (also WA, WI and WR)'), ('WR', 'Indonesia (also WA, WI and WQ)'), ('WS', 'Singapore'), ('Y', 'Australia (including Norfolk Island, Christmas Island, Cocos (Keeling) Islands and Australian Antarctic Territory)'), ('Z', 'Mainland China (except ZK and ZM)'), ('ZK', 'North Korea'), ('ZM', 'Mongolia')], max_length=2),
        ),
    ]
