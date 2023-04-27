from neo4j import GraphDatabase
from faker import Faker
import random

edgeDens = 0.4

faker = Faker()

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234567890"))
session = driver.session()

data = {}
gender = ["Male", "Female", "Other"]

with open('gplus_combined.txt') as f:
    lines = f.readlines()
    for line in lines:
        if(random.random() < edgeDens):
            continue
        us1, us2 = line.strip().split()
        if(data.get(us1) is None):
            data[us1] = (faker.name(),random.choice(gender))
        if(data.get(us2) is None):
            data[us2] = (faker.name(),random.choice(gender))
        query = f"MERGE (a:{data[us1][1]} " + "{name:$us1})" + f"MERGE (b:{data[us2][1]} " +"{name:$us2})" + f"MERGE (a)-[:FRIEND " + "{strength:"+ f"{random.random()}"+"}]-(b)" 
        session.run(query,us1=data[us1][0],us2=data[us2][0])
