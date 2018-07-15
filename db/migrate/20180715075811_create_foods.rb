class CreateFoods < ActiveRecord::Migration[5.2]
  def change
    create_table :foods do |t|
      t.string :name
      t.string :link
      t.string :location
      t.string :rating

      t.timestamps
    end
  end
end
