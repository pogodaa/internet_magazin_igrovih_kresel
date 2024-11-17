def index(request):
      context = {

            "tovars": [
                  # Офисные стулья

                  # Офисный стул YAPPI_SORO_23
                  {
                        'image': '{% static "img\katalog_tovars\ofisnie\YAPPI_Soro\YAPPI Soro.jpg" %}',
                        'href': "tovars:YAPPI_SORO_23",
                        'name': 'Офисный стул YAPPI_SORO_23',
                        'description': 'Компьютерное офисное кресло руководителя YAPPI Soro-23, ткань серо-бежевая',
                        'price': 19.264
                  },

                  # Стулья

                  # Стул Byroom_Office_EL_ff_VC1007O-B
                  {
                        'image': '{% static "img\katalog_tovars\stylia\Byroom Office\Byroom_Office_EL_ff_VC1007O.jpg" %}',
                        'name': 'Стул Byroom_Office_EL_ff_VC1007O-B',
                        'description': 'Офисное компьютерное кресло без подлокотников Byroom Office EL_ff VC1007O-B стул на колесиках, рабочее кресло для руководителя, взрослого и школьника',
                        'price': 2.991
                  },

                  # Детские стулья

                  # BUROKIDS_first
                  {
                        'image': '{% static "img\katalog_tovars\detskie\BUROKIDS_first\BUROKIDS_first.jpg" %}',
                        'name': 'BUROKIDS_first',
                        'description': 'Бюрократ Детское компьютерное кресло BUROKIDS, Космозавры, черный пластик',
                        'price': 5.383
                  },
                  
                  # Игровые кресла

                  # Zombie_KNIGHT_Smile
                  {
                        'image': '{% static "img\katalog_tovars\igrovie\Zombie_KNIGHT_Smile\Zombie_KNIGHT_Smile.jpg" %}',
                        'name': 'Zombie_KNIGHT_Smile',
                        'description': 'Кресло игровое Zombie KNIGHT Smile черный эко.кожа крестов. пластик',
                        'price': 16.355
                  },


            ]
      }