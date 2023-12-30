animal_specifics = {
    "id" : "integer auto gen",
    "gender" : "string",
    "birth_date" : "string",
    "created_at" :"aut-gen",
    "number_siblings": "number, 1,2,3,4",

}
animal_species ={
    "id" : "integer auto gen",
    "breed" : "varChar",
    "species" : "varChar"
}
animal_family = {
    "id" : "integer auto gen",
    "relation" : "varChar",
    "relation_id" : "foreign key to animal_specifics"
}
animal_history = {
    "id" : "integer auto gen",
    "created_at" :"aut-gen",
    "status" : "string",
    "notes" : "varChar"
}
feed_rations = {
    "id" : "integer auto gen",
    "brand_name" : "varChar",
    "notes" : "varChar",
    "created_at" :"aut-gen",
    "ingredient_label_ID": "foreign key, / number"
}