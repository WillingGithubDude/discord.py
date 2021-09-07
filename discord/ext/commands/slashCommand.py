from .core import Command

class slashCommand(Command):

  def __init__(self, token: str, bot: commands.Bot):
    self.token = token
    self.bot = bot

  def command(self, **kwargs):
    def inner(func):
      name = kwargs.get("name") if not None else func.__name__
      description = kwargs.get("description")
      @wraps(func)
      def wrapper(*args, **kwargs):
        url="https://discord.com/api/v8/applications/866074970323681290/commands"
        json = {
          "name": name,
          "type": 1,
          "description": description,
          "options": [
              {
                  "name": "animal",
                  "description": "The type of animal",
                  "type": 3,
                  "required": True,
                  "choices": [
                      {
                          "name": "Dog",
                          "value": "animal_dog"
                      },
                      {
                          "name": "Cat",
                          "value": "animal_cat"
                      },
                      {
                          "name": "Penguin",
                          "value": "animal_penguin"
                      }
                  ]
              },
              {
                  "name": "only_smol",
                  "description": "Whether to show only baby animals",
                  "type": 5,
                  "required": False
              }
            ]
          }
        headers = {
            "Authorization": f"Bot {self.token}"
        }
        r = requests.post(url, headers=headers, json=json)
        print(r)
        ctx = slashContext(bot=self.bot)
        asyncio.run(func(*args, **kwargs))
    return inner
