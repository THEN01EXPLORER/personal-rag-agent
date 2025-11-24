from dotenv import load_dotenv
load_dotenv('D:/capstone/.env')
import os
try:
    from google.ai.generativelanguage_v1beta import ModelServiceClient, ListModelsRequest
    from google.api_core.client_options import ClientOptions
    api_key = os.environ.get('GOOGLE_API_KEY')
    assert api_key, 'GOOGLE_API_KEY not set'
    client = ModelServiceClient(client_options=ClientOptions(api_key=api_key))
    resp = client.list_models(ListModelsRequest())
    for m in resp.models:
        print(m.name)
except Exception as e:
    print('ERR:', type(e).__name__, str(e))
