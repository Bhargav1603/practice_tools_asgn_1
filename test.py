import sentry_sdk

# Initialize Sentry
sentry_sdk.init(
    dsn="https://c68248fc01b51d45ea4c6cdccbc489af@o4507498200236032.ingest.de.sentry.io/4507498213802064", 
    traces_sample_rate=1.0  
)

def divide_by_zero():
    return 1 / 0

def main():
    try:
        divide_by_zero()
    except Exception as e:
     
        sentry_sdk.capture_exception(e)
        print("Exception captured and sent to Sentry")

if __name__ == "__main__":
    main()
