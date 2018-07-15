class ApplicationController < ActionController::Base

  def full_address(name,location)
    return  [name , location].compact.reject(&:empty?).join("")
  end
end
