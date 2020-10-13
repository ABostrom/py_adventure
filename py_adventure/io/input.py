



from typing import List


class CommandLineInterface():

    def request_input(self, input_message: str) -> str:
        return input(input_message)

    def parse_input(self, input_to_parse :str, valid_commands : List[str]) -> bool:
        inputs = input_to_parse.split(" ", maxsplit=1)

        if inputs[0] not in valid_commands:
            return False, None

        return True, {"command":inputs[0], "parameters": inputs[1]}

    
    def output(self, output : str) -> None:
        print(output)






