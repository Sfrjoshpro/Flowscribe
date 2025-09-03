"""
flowscribe Python API and CLI entry point
"""
import argparse
from .core import Session

def main():
    parser = argparse.ArgumentParser(description="flowscribe CLI")
    parser.add_argument("run", nargs="?", help="Start a new flowscribe session")
    parser.add_argument("--app", type=str, default="flowscribe-app", help="App name")
    parser.add_argument("--mode", type=str, default="default", help="Run mode")
    parser.add_argument("--tags", type=str, default="", help="Comma-separated tags")
    args = parser.parse_args()

    if args.run:
        session = Session(app_name=args.app, mode=args.mode, tags=args.tags.split(",") if args.tags else [])
        print(f"Started session: {session.run_id}")
        # Example: add a flow and event
        flow = session.start_flow("example/flow")
        from .core import Event
        flow.add_event(Event(event_type="checkpoint", flow_id=flow.flow_id, step="init"))
        session.end_session()
        print(f"Ended session: {session.run_id}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
