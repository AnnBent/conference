import sqlite3

conn = sqlite3.connect('conference.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS conference_participants(
    full_name TEXT
    academic_degree TEXT
    scientific_direction TEXT
    place_of_work TEXT
    department TEXT
    job_title TEXT
    country TEXT
    city TEXT
    address TEXT
    work_phone INTEGER
    e_mail TEXT);
''')
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS info_about_participation_in_conference(
    full_name TEXT
    speaker_or_participant TEXT
    data_of_mailing_invitation TEXT
    data_of_receipt_application TEXT
    topic TEXT
    mark_of_thesis TEXT
    data_arrived TEXT
    need_for_hotel TEXT
    data_of_departure TEXT);
''')
conn.commit()
cur.execute('''CREATE TABLE IF NOT EXISTS conference_info(
    name_of_conf TEXT
    data_of_conf TEXT
    location TEXT
    organizers TEXT
    sponsors TEXT
    number_of_days_conf INTEGER
    number_of_participants INTEGER
    number_of_speakers INTEGER);
''')
conn.commit()


