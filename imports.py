import mkdocs.commands.serve

def run_docs():
    print("🚀 Запускаю сервер документації напряму через код...")
    try:
        mkdocs.commands.serve.serve(config_file='mkdocs.yml', dev_addr='127.0.0.1:8000')
    except KeyboardInterrupt:
        print("\n🛑 Сервер зупинено. Гарного дня, бро!")
    except Exception as e:
        print(f"💥 Щось пішло не так: {e}")

if __name__ == "__main__":
    run_docs()