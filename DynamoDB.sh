# Create Table
aws dynamodb create-table
--attribute-definitions AttributeName=PIZ,AttributeType=S
--table-name TeethCounter
--key-schema AttributeName=PIZ,KeyType=HASH
--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1
