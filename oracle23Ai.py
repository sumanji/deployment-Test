import oracledb
import logging as log
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.oraclevs import OracleVS
from langchain_text_splitters import RecursiveCharacterTextSplitter

class OracleDB:

    def __init__(self):
        self.user = "myuser"
        self.pwd = "oracle123"
        self.dsn ="localhost/FREEPDB1"

    def getClient(self):
        """Returns the oracle db client"""
        try:
            _oracle_db_client = oracledb.connect(user=self.user, password=self.pwd, dsn=self.dsn)
            log.INFO("Client Connection Successful")
            return _oracle_db_client
        except Exception as ex:
            log.error("error while connecting db")
            return None


if __name__ == "main":
    oracledb = OracleDB()
    oracledb.getClient()






