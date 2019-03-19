from termcolor import colored


class Logger:

    SUPPORTED_COLORS = (
        'grey',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white'
    )

    SUPPORTED_ATTRIBUTES = (
        'bold',
        'dark',
        'underline',
        'blink',
        'reverse',
        'concealed',
    )

    def __init__(self, module_name, color, delimiter='-->'):
        self.name = module_name
        self.delimiter = delimiter
        if color not in self.SUPPORTED_COLORS:
            raise ValueError('Given color is not supported')
        else:
            self.color = color

    def log(self, message, attribute=None):
        if message == None:
            warning = colored('Message is not passed to the function', 'yellow', 'bold')
            print(warning)

        else:
            text = f'{self.delimiter} {self.name}: {message}'
            log_message = colored(text, self.color, None, attribute)
            print(log_message)
