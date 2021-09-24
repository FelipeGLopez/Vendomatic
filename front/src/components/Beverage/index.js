import React from "react";

const Beverage = (props) => {
  const { item, buyItem } = props;
  return (
    <div key={item.id}>
      <div className="col-sm-6">
        <div className="card" style={{ margin: "2%" }}>
          <div className="card-body">
            <h5 className="card-title">Beverage: {item.name}</h5>
            <div className="card-text">$ {item.value}</div>
            <div
              style={{ color: item.quantity === 0 ? "red" : null }}
              className="card-text"
            >
              Remaining: {item.quantity}
            </div>
            <div>
              <button
                className="btn btn-primary"
                onClick={() => buyItem(item.id, item.name)}
              >
                Buy {item.name}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Beverage;
