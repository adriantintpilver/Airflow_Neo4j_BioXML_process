neo4j_querys = {
    # query_create_and_return_relationship
    'query_create_and_return_relationship' : "CREATE (n1:node { name: $node1_name ,id: $node1_id, type: $node1_type, taxonomy_id: $node1_taxonomy_id  }) "
    "CREATE (n2:node { name: $node2_name ,id: $node2_id, type: $node2_type, taxonomy_id: $node2_taxonomy_id  }) "
    "CREATE (n1)-[: $relationtag { postition: '$postition' , status: '$status'  }]->(n2) "
    "RETURN n1, n2",
    # query_if_not_exist_create_and_return_relationship
    'query_if_not_exist_create_and_return_relationship' : 
    "MERGE (n1:node { name: $node1_name ,id: $node1_id, real_name: $node1_real_name, type: $node1_type, taxonomy_id: $node1_taxonomy_id })  "
    "MERGE (n2:node { name: $node2_name ,id: $node2_id, real_name: $node2_real_name, type: $node2_type, taxonomy_id: $node2_taxonomy_id })  "
    "MERGE (n1)-[: $relationtag { postition: '$postition' , status: '$status'  }]->(n2) ",
    # query_if_not_exist_create_and_return_relationship_reference
    'query_if_not_exist_create_and_return_relationship_reference' : 
    "MERGE (n1:node { name: $node1_name ,id: $node1_id, real_name: $node1_real_name, type: $node1_type, taxonomy_id: $node1_taxonomy_id })  "
    "MERGE (n2:node { name: $node2_name ,id: $node2_id, real_name: $node2_real_name, type: $node2_type, title: $title, scope: $scope, date: $date, volume: $volume, first: $first, last: $last })  "
    "MERGE (n1)-[: $relationtag { postition: '$postition' , status: '$status'  }]->(n2) ",
    # query_if_not_exist_create_and_return_relationship_reference_author
    'query_if_not_exist_create_and_return_relationship_reference_author' : 
    "MERGE (n1:node { name: $node1_name ,id: $node1_id, real_name: $node1_real_name, type: $node1_type, taxonomy_id: $node1_taxonomy_id })  "
    "MERGE (n2:node { name: $node2_name ,id: $node2_id, real_name: $node2_real_name, type: $node2_type, title: $title, scope: $scope, date: $date, volume: $volume, first: $first, last: $last })  "
    "MERGE (n2)-[: $relationtag { postition: '$postition' , status: '$status'  }]->(n1) ",
    # find_and_return_node
    'query_find_and_return_node' : "MATCH (n:node) "
    "WHERE n.name = $node_name AND n.id = $node_id AND n.type = $node_type AND n.taxonomy_id = $node_taxonomy_id "
    "RETURN n.name AS name, ID(n) as ID"
}