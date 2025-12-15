from ai_edge_litert.interpreter import Interpreter

interpreter = Interpreter(model_path="src/room_node/comfort_forecast.tflite")
interpreter.allocate_tensors()

inp = interpreter.get_input_details()[0]["index"]
out = interpreter.get_output_details()[0]["index"]

def get_prediction(x):
    interpreter.set_tensor(inp, x)
    interpreter.invoke()
    y = interpreter.get_tensor(out)[0]
    
    return float(y[0]), float(y[1])