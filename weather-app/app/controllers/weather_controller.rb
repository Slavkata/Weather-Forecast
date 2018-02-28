class WeatherController < ApplicationController
  def index
    `python ./vendor/setup.py 05.01.2018 ./vendor/export`
  end

  def predict
    time = DateTime.now.strftime("%k").to_i
    @date = time < 14 ? DateTime.now : DateTime.now + 1
    @date = @date.strftime("%d.%m.%Y")
    `python ./vendor/single_date_predictor.py #{@date} ./vendor/export`
    redirect_to "/weather/display?date=#{@date}"
  end

  def display
    require "csv"
    csv = CSV.read("./vendor/test_f.csv")
    @date = params['date']
    a = 0
    for i in 366..373 do
       if csv[1][i].to_i == 1
         a = i
         break
       end
    end

    a -= 365
    @time = []
    for i in 0..4 do
      @time.push(-1 + 3*(a - i))
    end

    @temperature = []
    i = 1
    CSV.foreach("./vendor/predi.csv") do |row|
      if i == 1
        i = 2
        next
      end
      @temperature.push(row[1].to_f.round(1))
    end

  end
end
