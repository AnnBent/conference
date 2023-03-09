import sqlite3

conn = sqlite3.connect('conferences.db')
cur = conn.cursor()
cur.execute('''DELETE FROM conference_participants;''')
cur.execute('''DELETE FROM info_about_participation_in_conference;''')
cur.execute('''DELETE FROM conference_info;''')
cur.execute('''CREATE TABLE IF NOT EXISTS conference_participants(
    full_name TEXT,
    academic_degree TEXT,
    scientific_direction TEXT,
    place_of_work TEXT,
    department TEXT,
    job_title TEXT,
    country TEXT,
    city TEXT,
    address TEXT,
    work_phone INTEGER,
    e_mail TEXT);
''')
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS info_about_participation_in_conference(
    full_name TEXT,
    speaker_or_participant TEXT,
    invitation TEXT,
    application TEXT,
    topic TEXT,
    thesis TEXT,
    arrived TEXT,
    hotel TEXT,
    departure TEXT);
''')
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS conference_info(
    name_of_conf TEXT,
    data_of_conf TEXT,
    location TEXT,
    organizers TEXT,
    sponsors TEXT,
    numb_of_days_conf INTEGER,
    numb_of_participants INTEGER,
    numb_of_speakers INTEGER);
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Костюченко Иван Дмитриевич',
    'Кандидат наук',
    'Физико-математическое направление',
    'БГУИР',
    'Кафедра информационных технологий автоматизированных систем',
    'Заведующий кафедрой',
    'Беларусь',
    'Минск',
    'Карла Либкнехта 132, кв. 45',
    '+375295639562',
    'kostik@gmail.com');
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Муха Владимир Степанович',
    'Доктор наук',
    'Техническое направление',
    'БГУИР',
    'Кафедра информационных технологий автоматизированных систем',
    'Профессор',
    'Беларусь',
    'Минск',
    'Партизанский проспект 26, кв. 48',
    '+375296957365',
    'muhavlad@gmail.com');
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Герман Олег Витольдович',
    'Кандидат наук',
    'Техническое направление',
    'БГУИР',
    'Кафедра информационных технологий автоматизированных систем',
    'Доцент',
    'Беларусь',
    'Минск',
    'Серая 5, кв. 4',
    '+375296584628',
    'germanoleg@gmail.com');
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Лапицкая Наталья Владимировна',
    'Кандидат наук',
    'Техническое направление',
    'БГУИР',
    'Кафедра программного обеспечения информационных технологий',
    'Заведующая кафедрой',
    'Беларусь',
    'Минск',
    'Интернациональная 26, кв. 36',
    '+375296568958',
    'lapickaya.com');
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Можей Наталья Павловна',
    'Кандидат наук',
    'Физико-математиское направление',
    'БГУИР',
    'Кафедра программного обеспечения информационных технологий',
    'Доцент',
    'Беларусь',
    'Минск',
    'Шафарнянская 76, кв. 76',
    '+375294367558',
    'nataliapavlovna.com');
''')
conn.commit()
cur.execute('''INSERT INTO conference_participants VALUES(
    'Давыдовский Анатолий Григорьевич',
    'Кандидат наук',
    'Биологическое направление',
    'БГУИР',
    'Кафедра программного обеспечения информационных технологий',
    'Доцент',
    'Беларусь',
    'Минск',
    'Притыцкого 75, кв. 61',
    '+375294333658',
    'davydovskiy.com');
''')
conn.commit()

cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Костюченко Иван Дмитриевич',
    'Докладчик',
    '28.02.2023',
    '01.03.2023',
    'Инновационные научные исследования в современном мире',
    '+',
    '24.03.2023',
    '+',
    '29.03.2023');
''')
conn.commit()
cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Муха Владимир Степанович',
    'Участник',
    '27.02.2023',
    '28.02.2023',
    '',
    '',
    '25.03.2023',
    '+',
    '29.03.2023');
''')
conn.commit()
cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Герман Олег Витольдович',
    'Участник',
    '26.02.2023',
    '28.02.2023',
    '',
    '',
    '25.03.2023',
    '+',
    '29.03.2023');
''')
conn.commit()
cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Лапицкая Наталья Владимировна',
    'Докладчик',
    '24.02.2023',
    '24.02.2023',
    'Приоритетные направления развития науки в современном мире',
    '+',
    '24.03.2023',
    '',
    '29.03.2023');
''')
conn.commit()
cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Можей Наталья Павловна',
    'Участник',
    '26.02.2023',
    '26.02.2023',
    '',
    '',
    '25.03.2023',
    '',
    '29.03.2023');
''')
conn.commit()
cur.execute('''INSERT INTO info_about_participation_in_conference VALUES(
    'Давыдовский Анатолий Григорьевич',
    'Участник',
    '25.02.2023',
    '26.02.2023',
    '',
    '',
    '25.03.2023',
    '+',
    '29.03.2023');
''')
conn.commit()

cur.execute('''INSERT INTO conference_info VALUES(
    'Инновационные научные исследования: теория, методология, тенденции развития',
    '27.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    25,
    3);
''')
conn.commit()
cur.execute('''INSERT INTO conference_info VALUES(
    'Теоретические и практические аспекты развития современной науки: теория, методология, практика',
    '21.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    30,
    3);
''')
conn.commit()
cur.execute('''INSERT INTO conference_info VALUES(
    'Теоретические и практические вопросы фундаментальных и прикладных научных исследований',
    '25.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    29,
    3);
''')
conn.commit()
cur.execute('''INSERT INTO conference_info VALUES(
    'Перспективные научные исследования: опыт, проблемы и перспективы развития',
    '15.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    40,
    3);
''')
conn.commit()
cur.execute('''INSERT INTO conference_info VALUES(
    'Технологические инновации и научные открытия',
    '19.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    25,
    3);
''')
conn.commit()
cur.execute('''INSERT INTO conference_info VALUES(
    'Актуальные вопросы инноваций и современные научные открытия',
    '17.03.2023',
    'RENAISSANCE MINSK HOTEL',
    'Дмитриева Вероника Викторовна, Новикова Анна Михайловна',
    'Альфа-Банк',
    1,
    35,
    3);
''')
conn.commit()
print("Справочник персоналий участников конференции:")
for i in cur.execute('''SELECT * FROM conference_participants;'''):
    print(i)
print("\nИнформация, связанная с участием в конференции:")
for i in cur.execute('''SELECT * FROM info_about_participation_in_conference;'''):
    print(i)
print("\nИнформация о конференции:")
for i in cur.execute('''SELECT * FROM conference_info;'''):
    print(i)
print("\nСписок докладчиков и темы их выступлений:")
for i in cur.execute('''SELECT full_name,topic
    FROM info_about_participation_in_conference 
    WHERE speaker_or_participant='Докладчик';'''):
    print(i)

cur.execute('''UPDATE conference_participants SET academic_degree='Доктор наук', scientific_direction='Техническое направление'
    WHERE full_name='Костюченко Иван Дмитриевич';''')
conn.commit()
cur.execute('''DELETE FROM conference_info WHERE numb_of_participants=35''')
conn.commit()
cur.close()
conn.close()
