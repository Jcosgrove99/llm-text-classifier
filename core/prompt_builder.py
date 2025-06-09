

class PromptBuilder(): 
    def __init__(self) -> None:
        pass

    def build_user_prompt(self, prompt:str, categories:list[str], input_text:list[str]) -> str:
        categories_text_str = ",".join(categories)
        input_text_str = ",".join(input_text)
        user_prompt = f'''
                        {prompt}\n
                        # Place the input text into only one of the following categories:\n
                        {categories_text_str}\n
                        # Here is the comma seperate input text. For each input select one category.\n
                        {input_text_str}
                    '''
        return user_prompt
        

