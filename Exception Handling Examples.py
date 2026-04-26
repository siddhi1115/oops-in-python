def simple_data_check():
    data = [10, 20]
    info = {"id": 101}

    try:
        val = int(input("Number: "))
        print(10 / val)

        print(data[1]) 
        print(info["age"])

    except ValueError: 
        print("Error: Only numbers accepted!")
    except ZeroDivisionError: 
        print("Error: Division by Zero!")
    except IndexError: 
        print("Error: List index is wrong!")
    except KeyError: 
        print("Error: Key not found!")
    except Exception as e: 
        print(f"Error: {e}") 

simple_data_check()