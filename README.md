# Taxid_api
 A basic exercise based on an api that found some data and related metadeta in a mongo database, using some end points

## 1. Run docker compose

The docker compose file run the basic mongo container.
```
cd mongodb
docker-compose up -d
```
## 2. Load the test files on mongodb

the python script take the datset from the  json file "mongodb/database/gff_dataset.json" and insert the entries in the mongodb using [PyMongo](https://github.com/mongodb/mongo-python-driver).
```
python3 create_dataset.py
```

## 3. Run the Rest Api

The python script run the basic rest api (using [Flask](https://github.com/pallets/flask)).
```
cd ../
python3 GFF_from_taxid.py
```

## 4. end points check

After the procedure the api response to three very simple end points, that return some information from the mongodb.
```
curl http://127.0.0.1:5000/taxons --> return the list of all the taxons available
curl http://127.0.0.1:5000/taxons/taxid --> return all the info related to a certain taxid
curl http://127.0.0.1:5000/files/taxid --> return the gff file related to the taxid 
```
