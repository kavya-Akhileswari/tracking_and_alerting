#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant("b1fa120c-cb30-49bc-bc44-23e08cf5cb05-bluemix",
                  "7f0cc21a0fe7673bd4921baacd32e8702b81bdaf33e5a11f2ec088a3afcdc2b3",
                  url="https://b1fa120c-cb30-49bc-bc44-23e08cf5cb05-bluemix:7f0cc21a0fe7673bd4921baacd32e8702b81bdaf33e5a11f2ec088a3afcdc2b3@b1fa120c-cb30-49bc-bc44-23e08cf5cb05-bluemix.cloudantnosqldb.appdomain.cloud")

client.connect()



def main(dict):
    databaseName = "vehicle_tracking"
    myDatabaseDemo = client.create_database(databaseName)
    if myDatabaseDemo.exists():
        print("'{0}' successfully created.\n".format(databaseName))
    record={"latitude":dict['latt'],"longitude":dict['longi']}
    newDocument = myDatabaseDemo.create_document(record)
    return { "Response": "Document successfully created."}


    


