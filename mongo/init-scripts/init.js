bdd = db.getSiblingDB("blog_db");

bdd.createCollection("posts", { 
    validator: {
        $jsonSchema: {
            bsonType: "object",
            title: "Blog",
            required: [ "titre", "auteur", "vue" ],
            properties: {
                titre: {
                    bsonType: "string",
                    description: "'titre' must be a string and is required"
                },
                auteur: {
                    bsonType: "string",
                    description: "'auteur' must be a string and is required"
                },
                vue: {
                    bsonType: "int",
                    description: "'vue' must be a integer and is required"
                }
            }
        }
    }
});

bdd.posts.insertOne({ titre: "Pomme", auteur: "Samuel", vue: 999 });
bdd.posts.insertOne({ titre: "Poire", auteur: "Matias", vue: 99 });
bdd.posts.insertOne({ titre: "Citron", auteur: "William", vue: 9998 });
bdd.posts.insertOne({ titre: "Orange", auteur: "Louis", vue: 979 });
bdd.posts.insertOne({ titre: "Kiwi", auteur: "Geoffrey", vue: 299 });