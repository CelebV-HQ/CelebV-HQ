import json
import pymysql
import time


class CelebVDB:

    def __init__(self):
        self.dbname = "sys"
        self.user = "root"
        self.port = 3306
        self.password = '123456'
        self.host = '127.0.0.1'
        self.conn = None
        self.table_name = "cele_table"

    def create_table(self, total_columns):
        cursor = self.conn.cursor()
        table_str = ''
        for i, value in enumerate(total_columns):
            table_str = table_str + f"{value}       varchar(256) null"
            if i < (len(total_columns) - 1):
                table_str = table_str + ','
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
            cursor.execute(sql, list(data.values()))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()


# "ytb_id","start_sec","end_sec","top","bottom","left","right","appearance","action","sep_flag","labels","version"
def parse_json_to_dict(val):
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


if __name__ == "__main__":
    cele_db = CelebVDB()
    cele_db.get_connection()

    json_path = "celebvhq_info.json"
    with open(json_path) as f:
        data_dict = json.load(f)
    # appearance_list = data_dict["meta_info"]["appearance_mapping"]
    # action_list = data_dict["meta_info"]["action_mapping"]
    total_columns = ["ytb_id", "start_sec", "end_sec", "top", "bottom", "left_pt",
                     "right_pt", "sep_flag", "labels", "version"]  # + appearance_list + action_list
    cele_db.create_table(total_columns)
    # insert data to table
    for key, val in data_dict['clips'].items():
        db_item = parse_json_to_dict(val)
        cele_db.insert_data(db_item)

    cele_db.close_connection()
