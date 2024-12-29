# 🖩 **Calculator GUI with Networking**

A simple calculator GUI client that communicates with a server to perform basic arithmetic operations. The client sends expressions to the server, which evaluates them and returns the result.

---

## 📂 **Files**

- **🖥️ `calci_gui_client.py`**: Client-side script providing a graphical user interface for the calculator.  
- **🔗 `calci_gui_server.py`**: Server-side script that evaluates expressions sent by the client.  

---

## 🛠️ **Requirements**

- 🐍 **Python 3.x**
- 📦 **Tkinter** (usually included with Python)  
- 🌐 **Network connection**  

---

## ⚙️ **Setup**

1. Clone the repository:  
    ```sh
    git clone https://github.com/dharunm236/calculator-networking.git
    cd calculator-networking
    ```

2. Ensure Python is installed. You can download it from [python.org](https://www.python.org/).

---

## 🚀 **Running the Server**

1. Open a terminal or command prompt.  
2. Navigate to the directory containing the scripts.  
3. Start the server:  
    ```sh
    python calci_gui_server.py
    ```

---

## 💻 **Running the Client**

1. Open another terminal or command prompt.  
2. Navigate to the directory containing the scripts.  
3. Start the client:  
    ```sh
    python calci_gui_client.py
    ```

---

## 🎯 **Usage**

1. The client window will open with a basic calculator interface.  
2. Enter numbers and operations as you would with a standard calculator.  
3. The client sends the expression to the server for evaluation.  
4. The server evaluates the expression and sends the result back to the client.  
5. The result is displayed in the client window.

---

## ✨ **Features**

- ✅ Basic arithmetic operations: addition, subtraction, multiplication, division.  
- ✅ Bitwise operations: AND, OR, NOT.  
- ✅ Simple GUI using Tkinter.  
- ✅ Network communication using sockets.

---

## 📸 **Sample Images**

### **Client Interface**
![Client Interface](assets/calci_gui.png)


---

## 🤝 **Contributing**

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Make your changes.  
4. Commit your changes (`git commit -am 'Add new feature'`).  
5. Push to the branch (`git push origin feature-branch`).  
6. Create a new Pull Request.

---

## 🖋️ **Authors**

- Dharun

---

## 🙏 **Acknowledgments**

- Thanks to the Python community for their valuable resources and support.
