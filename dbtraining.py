import sqlite3

class SQLighter:
    
    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
    
   
    def training_exists(self, user_id):
        """Проверяем есть ли пользователь в базе"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `trainingrun` WHERE `user_id` = ?", (user_id,)).fetchal()
            return bool(len(result))
        
    def add_user(self, user_id, status = True):
        """Добавляем нового пользователя в БД"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `trainingrun` (`user_id`, `status`) VALUES (?,?)", (user_id, status))
        
    def update_user(self, user_id, status):
         with self.connection:
            return self.cursor.execute("UPDATE 'trainingrun' SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
    
         
    