import React from "react";
import axios from "axios";

const BeverageList = (props) => {
  const { items, setCoins, setText } = props;

  const buyItem = (id, name) => {
    axios
      .put(`http://localhost:8000/inventory/${id}/`)
      .then((response) => response.headers)
      .then(
        (data) => {
          setCoins(data["x-coins"]);
        },
        (error) => {
          if (error.response.status === 404) {
            setText(
              `You have ${error.response.headers["x-coins"]} coins!\nThere are no ${name} beverages left!`
            );
          } else if (error.response.status === 400) {
            setText(`You have ${error.response.headers["x-coins"]} coins!`);
          } else {
            console.log(error);
          }
        }
      );
  };

  return (
    items.length >= 0 && (
      <>
        {items.map((item) => {
          return (
            <div key={item.id}>
              <div>Beverage: {item.name}</div>
              <div>$ {item.value}</div>
              <div>Remaining: {item.quantity}</div>
              <div>
                <button onClick={() => buyItem(item.id, item.name)}>
                  Buy {item.name}
                </button>
              </div>
            </div>
          );
        })}
      </>
    )
  );
};

export default BeverageList;
