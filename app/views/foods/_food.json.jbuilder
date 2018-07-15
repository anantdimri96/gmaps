json.extract! food, :id, :name, :link, :location, :rating, :created_at, :updated_at
json.url food_url(food, format: :json)
