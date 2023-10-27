"""
A sample Hello World server.
"""
import os
from flask import Flask, render_template,request,jsonify
import google.auth
import google.auth.transport.requests
from google.cloud import discoveryengine_v1beta


# pylint: disable=C0103
app = Flask(__name__)

@app.route('/sample', methods=['POST'])
def index():
    print ("then post updated")

    # return (results)
    data = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        } 
  
    return jsonify(data)
@app.route('/search', methods=['POST'])
def search():
    datastore_id = "google-store-search-en-ds_1697713466392"
    project_id = "emea-ccai-demo"
    location = "global"
    collection_id = "default_collection"
    serving_config_id = "default_serving_config"
    base_url = "https://discoveryengine.googleapis.com/v1beta"
    serving_config = f"projects/{project_id}/locations/{location}/collections/{collection_id}/dataStores/{datastore_id}/servingConfigs/{serving_config_id}"
    endpoint = f"{base_url}/{serving_config}:search"
    # data = { 
    #         "dummy_number" : 15, 
    #         "dummy_subject" : "Data Structures and Algorithms", 
    #     }  
    data = request.get_json()
    print(f"The request data {data}")
    query = data.get("query")
    num_results = data.get("num_results")

    client = discoveryengine_v1beta.SearchServiceClient()

    req = discoveryengine_v1beta.SearchRequest(
        serving_config=serving_config,
        query=query,
        page_size=num_results,
        
    )

    res = client.search(req)
    results = []
    for result in res.results:
        doc = result.document
        doc_dict = {}
        doc_dict['name'] = doc.name
        doc_dict['title'] = doc.derived_struct_data['title']
        doc_dict['link'] = doc.derived_struct_data['link']
        # doc_dict['snippet'] = doc.derived_struct_data['snippets'][0]['snippet']
        results.append(doc_dict)

    data = {"results": results}
    data_dummy = { 
            "Modules" : 15, 
            "Subject" : "Data Structures and Algorithms", 
        }

  
    return jsonify(data)
    


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')