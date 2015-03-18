__author__ = 'Xuefeng Zhu'
from portfolio.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)