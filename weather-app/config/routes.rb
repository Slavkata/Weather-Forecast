Rails.application.routes.draw do
  post 'weather/index'

  get 'weather/predict'

  get 'weather/display'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
