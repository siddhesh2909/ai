program StockMarketTradingSystem;
uses
SysUtils;
function AskQuestion(prompt: string): string;
var
answer: string;
begin
Write(prompt + ' ');
ReadLn(answer);
AskQuestion := answer;
end;
function Evaluate(trend, fundamentals, indicators: string): boolean;
begin
Evaluate := (LowerCase(trend) = 'upwards') and
(LowerCase(fundamentals) = 'strong') and
(LowerCase(indicators) = 'positive');
end;
procedure PrintResult(shouldBuy: boolean);
begin
if shouldBuy then
WriteLn('Recommendation: Buy the stock!')
else
WriteLn('Recommendation: Do not buy the stock.');
end;
var
Trend, Fundamentals, Indicators: string;
shouldBuy: boolean;
begin
WriteLn('Welcome to the Stock Market Trading System!');
WriteLn('Please answer the following questions:');
Trend := AskQuestion('What is the current market trend? (Upwards/Downwords):');
Fundamentals := AskQuestion('How are the fundamentals of the company? (strong/
weak):');
Indicators := AskQuestion('What do the technical indicators suggest? (positive/
negative):');
shouldBuy := Evaluate(Trend, Fundamentals, Indicators);
PrintResult(shouldBuy);
end.
