import json
import pymysql
import time
from tqdm import tqdm

# prerequisites: docker pull mysql; docker run -itd --name mysql-test -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql

class CelebVDB:

    def __init__(self):
        self.dbname = "sys"
        self.user = "root"
        self.port = 3306
        self.password = '123456'
        self.host = '127.0.0.1'
        self.conn = None

    def create_table(self):
        total_columns = ["ytb_id", "start_sec", "end_sec", "top", "bottom", "left_pt",
                         "right_pt", "sep_flag", "labels", "version"]
        cursor = self.conn.cursor()
        table_str = ''
        for i, value in enumerate(total_columns):
            table_str = table_str + f"{value}       varchar(256) null"
            if i < (len(total_columns) - 1):
                table_str = table_str + ','
        self.table_name = "cele_table"
        sql = f'CREATE TABLE {self.table_name} (id  int auto_increment primary key,{table_str})'
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()

    def create_emotion_table(self):
        total_columns = ["ytb_id", "start_sec", "end_sec", "emotion"]
        cursor = self.conn.cursor()
        table_str = ''
        for i, value in enumerate(total_columns):
            table_str = table_str + f"{value}       varchar(256) null"
            if i < (len(total_columns) - 1):
                table_str = table_str + ','
        self.table_name = "emotion_table"
        sql = f'CREATE TABLE {self.table_name} (id  int auto_increment primary key,{table_str})'
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()

    def get_connection(self):
        while True:
            try:
                self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                            password=self.password, database=self.dbname, charset='utf8')
                break
            except Exception as e:
                print('wait for db.')
                time.sleep(3)

    def close_connection(self):
        self.conn.close()

    def insert_data(self, data):
        cursor = self.conn.cursor()
        data_type = "%s," * (len(data) - 1) + "%s"
        column = ''
        for i, value in enumerate(data.keys()):
            column = column + str(value)
            if i < (len(data) - 1):
                column = column + ','
        sql = f"INSERT INTO {self.table_name}({column}) VALUES ({data_type})"
        try:
            cursor.execute(sql, list(map(str, data.values())))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()

    def parse_json_to_dict(self, val):
        # "ytb_id","start_sec","end_sec","top","bottom","left","right","appearance","action","sep_flag","labels","version"
        db_item = dict()
        db_item["ytb_id"] = val['ytb_id']

        db_item["start_sec"] = val['duration']['start_sec']
        db_item["end_sec"] = val['duration']['end_sec']

        db_item['top'] = val['bbox']['top']
        db_item['bottom'] = val['bbox']['bottom']
        db_item['left_pt'] = val['bbox']['left']
        db_item['right_pt'] = val['bbox']['right']

        # tmp = val['attributes']['appearance']
        # for index, appearance in enumerate(appearance_list):
        #     db_item[appearance] = tmp[index]
        #
        # actions = val['attributes']['action']
        # for index, action in enumerate(action_list):
        #     db_item[action] = actions[index]

        emotion = val['attributes']['emotion']
        db_item['sep_flag'] = emotion['sep_flag']
        db_item['labels'] = emotion['labels']

        db_item['version'] = val['version']
        return db_item

    def extract_emotion_data(self, val):
        data_items = []
        emotion = val['attributes']['emotion']
        emotion_label = emotion['labels']
        start_sec = val['duration']['start_sec']
        end_sec = val['duration']['end_sec']
        if isinstance(emotion_label, list):
            for item in emotion_label:
                db_item = dict()
                db_item["ytb_id"] = val['ytb_id']
                db_item["start_sec"] = start_sec + item['start_sec']
                db_item["end_sec"] = start_sec + item['end_sec']
                db_item["emotion"] = item['emotion']
                data_items.append(db_item)
        elif isinstance(emotion_label, str):
            db_item = dict()
            db_item["ytb_id"] = val['ytb_id']
            db_item["start_sec"] = start_sec
            db_item["end_sec"] = end_sec
            db_item["emotion"] = emotion_label
            data_items.append(db_item)

        return data_items


if __name__ == "__main__":
    cele_db = CelebVDB()
    cele_db.get_connection()

    json_path = "celebvhq_info.json"
    with open(json_path) as f:
        data_dict = json.load(f)
    # appearance_list = data_dict["meta_info"]["appearance_mapping"]
    # action_list = data_dict["meta_info"]["action_mapping"]

    # cele_db.create_table()
    # print("create general table successfully!")
    # print("Starting insert the data to general table...")
    # for key, val in data_dict['clips'].items():
    #     db_item = cele_db.parse_json_to_dict(val)
    #     cele_db.insert_data(db_item)
    # print("Inserting all data to general table successfully!")

    cele_db.create_emotion_table()
    print("create emotion table successfully!")
    print("Starting insert the data to emotion table...")
    for key, val in tqdm(data_dict['clips'].items()):
        db_items = cele_db.extract_emotion_data(val)
        for db_item in db_items:
            cele_db.insert_data(db_item)
    print("Inserting all data to emotion table successfully!")
    cele_db.close_connection()
